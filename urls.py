"""
URL Configuration for Tasks App

This file defines the URL patterns for the tasks application.
It maps URLs to their corresponding views.
"""

from django.urls import path
from . import views

# URL patterns for the tasks app
urlpatterns = [
    # Home page - view all tasks
    # URL: /
    path('', views.task_list, name='task_list'),
    
    # Add a new task
    # URL: /add/
    path('add/', views.add_task, name='add_task'),
    
    # Toggle task completion status
    # URL: /toggle/<task_id>/
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    
    # Delete a task
    # URL: /delete/<task_id>/
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]

