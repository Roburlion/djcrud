from django.shortcuts import render
from django.http import HttpResponse
from .models import ButtonLog, CustomerAging
from django.template.loader import render_to_string
from django.http import JsonResponse
import pandas as pd
from django.db import connection

def get_customer_aging():
    return ButtonLog.objects.all().order_by('-id')[:10]

def button_upload(request):
    if request.method == 'POST':
        try:
            # Get the uploaded file
            uploaded_file = request.FILES.get('file')
            
            # Determine file type and read accordingly
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(uploaded_file)
            else:
                return JsonResponse({'error': 'Unsupported file format'}, status=400)

            # Process each row
            for index, row in df.iterrows():
                try:
                    timestamp = pd.to_datetime(row['timestamp'])
                    timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                    print(f"Index: {index} Row: {row} timestamp: {timestamp_str}")
                    query = "INSERT INTO home_buttonlog (pressed_at) VALUES (%s);"
                    with connection.cursor() as cursor:
                        cursor.execute(query, [timestamp_str])
                except Exception as e:
                    print(f"Error processing row {index}: {e}")
                    continue

            return JsonResponse({
                'status': 'success',
                'message': f'Processed {len(df)} records'
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return render(request, 'your_template.html')  # Replace with your template name