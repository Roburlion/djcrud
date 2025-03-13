from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('', views.home_page, name='home_page'),  # Maps the root URL to the homepage
    path('htmx_page', views.htmx_page, name='htmx_page'),
    path('upload_button_page', views.upload_button_page, name='upload_button_page'),
    path('upload_aging_page', views.upload_aging_page, name='upload_aging_page'),
    # APIs
    path('button_upload', views.button_upload, name='button_upload'),
    path('customer_aging_upload', views.customer_aging_upload, name='customer_aging_upload'),
]