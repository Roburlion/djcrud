from django.shortcuts import render
from django.http import HttpResponse
from .models import ButtonLog, WOB
from django.template.loader import render_to_string
from django.http import JsonResponse
import pandas as pd
from django.db import connection

def get_wobs():
    return WOB.objects.all()[:10]

def transform_customer_aging(file):
    # Read Excel file
    df = pd.read_excel(file, skiprows=2, usecols="A, C:D, H:Q", dtype={
        "Days Old":                       "Int64",
        "Batch ID":                       object,
        "Mfg Batch ID":                   object,
        "Mfg Batch Creation":             "Int64",
        "Mfg Batch Create Complete":      "Int64",
        "Ready for Fulfillment":          "Int64",
        "Tasks in Progress":              "Int64",
        "At Printer":                     "Int64",
        "Error in Print Tasks":           "Int64",
        "Print Success":                  "Int64",
        "Error in Printing":              "Int64",
        "Total Orders (blanks)":          "Int64",
        "Work Orders":                    "Int64",
    })

    # Pivot status columns to a single column
    status_columns = [
        "Mfg Batch Creation",
        "Mfg Batch Create Complete",
        "Ready for Fulfillment",
        "Tasks in Progress",
        "At Printer",
        "Error in Print Tasks",
        "Print Success",
        "Error in Printing",
        "Other"
    ]

    df.insert(loc=11, column='Other', value=1)
    df["status"] = df[status_columns].idxmax(axis=1, skipna=True)
    df = df.drop(columns=status_columns)

    # Rename columns
    df.columns = ["age", "wob", "batch", "order_qty", "page_qty", "status"]

    # Reorder columns
    df = df[["wob", "batch", "status", "age", "order_qty", "page_qty"]]

    # Fill missing values
    df.age = df.age.fillna(0)
    df.order_qty = df.order_qty.fillna(1)
    df.batch = df.batch.fillna('')

    # Add uploaded_at column
    df['uploaded_at'] = pd.to_datetime("now", utc=True)
    return df

def upload_wobs(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES.get('file')
            print(f"Uploaded file: {uploaded_file}")
            df = transform_customer_aging(uploaded_file)
            print(f"Transformed DataFrame:\n{df.head()}")
            customer_aging_records = [
                WOB(
                    wob=row['wob'],
                    batch=row['batch'],
                    status=row['status'],
                    age=row['age'],
                    order_qty=row['order_qty'],
                    page_qty=row['page_qty'],
                    uploaded_at=row['uploaded_at']
                )
                for _, row in df.iterrows()
            ]

            WOB.objects.bulk_create(
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

