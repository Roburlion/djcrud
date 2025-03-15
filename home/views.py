# home/views.py
from django.shortcuts import render
from django.template.loader import render_to_string
from .utils_button import button_upload, get_button_logs, log_button, log_htmx_button
from .utils_rocket import customer_aging_upload, get_wobs

def home_page(request):
    # Get updated logs
    button_logs = get_button_logs()
    return render(request, 'home/home_page.html', {'button_logs': button_logs})

def htmx_page(request):
    # Get updated logs
    button_logs = get_button_logs()
    return render(request, 'home/htmx_page.html', {'button_logs': button_logs})

def upload_button_page(request):
    return render(request, 'home/upload_button_page.html')

def upload_aging_page(request):
    return render(request, 'home/upload_aging_page.html')

def rolls_page(request):
    return render(request, 'home/rolls_page.html')