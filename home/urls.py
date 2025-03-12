from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),  # Maps the root URL to the homepage
    path('htmx_page', views.htmx_page, name='htmx_page'),
    path('upload_page', views.upload_page, name='upload_page'),
    path('aging_upload', views.aging_upload, name='aging_upload'),
]