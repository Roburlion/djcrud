from django.shortcuts import render
from django.http import HttpResponse
from .models import ButtonLog
from django.template.loader import render_to_string

def get_button_logs():
    """Helper function to get button logs in a consistent way."""
    return ButtonLog.objects.all().order_by('-pressed_at')[:10]

def home_page(request):
    # Get updated logs
    button_logs = get_button_logs()
    return render(request, 'home/home_page.html', {'button_logs': button_logs})

def htmx_page(request):
    # Get updated logs
    button_logs = get_button_logs()
    return render(request, 'home/htmx_page.html', {'button_logs': button_logs})

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