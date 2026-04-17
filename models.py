"""
Task Model - Defines the database schema for tasks

This module contains the Task model which represents a to-do item.
Each task has a title, description, creation timestamp, and completion status.
"""

from django.db import models
from django.utils import timezone


class Task(models.Model):
    """
    Task Model - Represents a to-do item in the task management system.
    
    Fields:
        title (CharField): The task title (required, max 200 characters)
        description (TextField): Detailed description of the task (optional)
        created_at (DateTimeField): Timestamp when the task was created (auto-set)
        completed (BooleanField): Whether the task is completed (default: False)
    
    Methods:
        __str__: Returns the task title as string representation
    """
    
    # Title field - required, max 200 characters
    title = models.CharField(max_length=200, help_text="Enter task title")
    
    # Description field - optional (blank=True, null=True)
    description = models.TextField(blank=True, null=True, help_text="Enter task description (optional)")
    
    # Created_at - automatically set to current time when task is created
    created_at = models.DateTimeField(default=timezone.now, help_text="Timestamp when task was created")
    
    # Completed - boolean field to track if task is done, default is False
    completed = models.BooleanField(default=False, help_text="Mark as completed")
    
    class Meta:
        # Order tasks by creation date (newest first)
        ordering = ['-created_at']
        # Verbose name for the model
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self):
        """Return the task title as string representation"""
        return self.title

