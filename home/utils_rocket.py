from django.shortcuts import render
from django.http import HttpResponse
from .models import ButtonLog, WOBs
from django.template.loader import render_to_string
from django.http import JsonResponse
import pandas as pd
from django.db import connection

def get_wobs():
    return WOBs.objects.all()[:10]

def transform_load_customer_aging(file):
    df = pd.read_excel(file, skiprows=2, usecols="A, C:D, H:Q")
    print(f"DataFrame shape: {df.shape}")
    # List of columns to pivot
    status_columns = [
        "Mfg Batch Creation",
        "Mfg Batch Create Complete",
        "Ready for Fulfillment",
        "Tasks in Progress",
        "At Printer",
        "Error in Print Tasks",
        "Print Success",
        "Error in Printing"
    ]

    # Replace NaN with 0 in these columns to ensure idxmax works
    df[status_columns] = df[status_columns].fillna(0)

    # Create the "status" column with the name of the column containing 1
    df["status"] = df[status_columns].idxmax(axis=1)

    # Optionally, drop the original columns if you no longer need them
    df = df.drop(columns=status_columns)

    df.columns = ["age", "wob", "batch", "order_qty", "page_qty", "status"]
    df = df[["wob", "batch", "status", "age", "order_qty", "page_qty"]]

    df.age = df.age.fillna(0)

    df.order_qty = df.order_qty.fillna(1)

    df['uploaded_at'] = pd.to_datetime("now", utc=True)

    return df

def customer_aging_upload(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES.get('file')
            print(f"Uploaded file: {uploaded_file}")
            df = transform_load_customer_aging(uploaded_file)
            print(f"Transformed DataFrame:\n{df.head()}")
            customer_aging_records = [
                WOBs(
                    wob=row['wob'],
                    batch=None if pd.isna(row['batch']) else row['batch'],
                    status=row['status'],
                    age=row['age'],
                    order_qty=row['order_qty'],
                    page_qty=row['page_qty'],
                    uploaded_at=row['uploaded_at']
                )
                for _, row in df.iterrows()
            ]

            WOBs.objects.bulk_create(
                customer_aging_records,
                update_conflicts=True,
                update_fields=['batch', 'status', 'age', 'order_qty', 'page_qty', 'uploaded_at'],  # Fields to update on conflict
                unique_fields=['wob'],  # Field(s) that define a conflict
            )

            return JsonResponse({'success': 'Data imported successfully'})

        except Exception as e:
            print(f"Error during upload: {e}")
            return JsonResponse({'error': str(e)}, status=400)
    
    return render(request, 'your_template.html')  # Replace with your template name

