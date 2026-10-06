from django.urls import path
from . import views

urlpatterns = [
    path('', views.gradebook_dashboard, name='dashboard'),
]