from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrape, name='home'),
    path('delete/', views.clear, name=''),
]