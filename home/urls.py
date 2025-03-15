from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('', views.home_page, name='home_page'),  # Maps the root URL to the homepage
    path('htmx_page', views.htmx_page, name='htmx_page'),
    path('upload_button_page', views.upload_button_page, name='upload_button_page'),
    path('upload_aging_page', views.upload_aging_page, name='upload_aging_page'),
    path('rolls_page', views.rolls_page, name='rolls_page'),
    # APIs
    path('button_upload', views.button_upload, name='button_upload'),
    path('upload_wobs', views.upload_wobs, name='upload_wobs'),
]