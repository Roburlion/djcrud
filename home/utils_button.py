from django.shortcuts import render
from django.http import HttpResponse
from .models import ButtonLog
from django.template.loader import render_to_string
from django.http import JsonResponse
import pandas as pd
from django.db import connection

def get_button_logs():
    """Helper function to get button logs in a consistent way."""
    return ButtonLog.objects.all().order_by('-id')[:10]

def log_button(request):
    ButtonLog.objects.create()
    return HttpResponse("Button pressed and logged.")

def log_htmx_button(request):
    """Handle button press: create a log entry and return appropriate response."""
    # Create a new ButtonLog entry
    ButtonLog.objects.create()
    
    # Get updated logs
    button_logs = get_button_logs()
    
    # If this is an HTMX request, return just the table fragment
    if 'hx-request' in request.headers:
        html = render_to_string(
            'home/_button_log_table.html',
            {'button_logs': button_logs}
        )
        return HttpResponse(html)
    
    # For non-HTMX requests, return the full HTMX page
    return render(request, 'home/htmx_page.html', {'button_logs': button_logs})

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