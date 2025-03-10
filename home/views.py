from django.shortcuts import render
from django.http import HttpResponse
from .models import ButtonLog

# Create your views here.
# def home_page(request):
#     return render(request, 'home/home_page.html')

def home_page(request):
    # Get all ButtonLog entries, ordered by pressed_at descending (newest first)
    button_logs = ButtonLog.objects.all().order_by('-pressed_at')
    return render(request, 'home/home_page.html', {'button_logs': button_logs})

def log_button(request):
    ButtonLog.objects.create()
    return HttpResponse("Button pressed and logged.")