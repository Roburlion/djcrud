from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),  # Maps the root URL to the homepage
    path('htmx_page', views.htmx_page, name='htmx_page'),
]