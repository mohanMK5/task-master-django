"""
Views - Handle the logic for task management

This module contains Django views that handle:
- Displaying all tasks (home page)
- Adding new tasks
- Toggling task completion status
- Deleting tasks
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Task


def task_list(request):
    """
    Home page view - Display all tasks
    
    Retrieves all tasks from the database, ordered by creation date (newest first),
    and renders them using the task_list.html template.
    
    Args:
        request: HttpRequest object
        
    Returns:
        Rendered HTML template with all tasks
    """
    # Get all tasks, ordered by creation date (newest first)
    tasks = Task.objects.all().order_by('-created_at')
    
    # Count tasks for display
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = total_tasks - completed_tasks
    
    # Context dictionary to pass to template
    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
    }
    
    return render(request, 'tasks/task_list.html', context)


def add_task(request):
    """
    Add a new task
    
    Handles POST request to create a new task.
    Redirects to home page after successful creation.
    
    Args:
        request: HttpRequest object
        
    Returns:
        Redirect to home page
    """
    if request.method == 'POST':
        # Get title from form data (required)
        title = request.POST.get('title', '').strip()
        
        # Get description from form data (optional)
        description = request.POST.get('description', '').strip()
        
        # Validate title - it's required
        if title:
            # Create new task
            Task.objects.create(
                title=title,
                description=description if description else ''  # Store empty string if no description
            )
        
        # Redirect to home page after adding task
        return redirect('task_list')
    
    # If not POST, redirect to home
    return redirect('task_list')


def toggle_task(request, task_id):
    """
    Toggle task completion status
    
    Finds the task by ID and toggles its completed status.
    Then redirects to the home page.
    
    Args:
        request: HttpRequest object
        task_id: ID of the task to toggle
        
    Returns:
        Redirect to home page
    """
    # Get the task by ID, or return 404 if not found
    task = get_object_or_404(Task, id=task_id)
    
    # Toggle the completed status
    task.completed = not task.completed
    
    # Save the updated task
    task.save()
    
    # Redirect back to home page
    return redirect('task_list')


def delete_task(request, task_id):
    """
    Delete a task
    
    Finds the task by ID, deletes it from the database,
    and redirects to the home page.
    
    Args:
        request: HttpRequest object
        task_id: ID of the task to delete
        
    Returns:
        Redirect to home page
    """
    # Get the task by ID, or return 404 if not found
    task = get_object_or_404(Task, id=task_id)
    
    # Delete the task
    task.delete()
    
    # Redirect back to home page
    return redirect('task_list')

