import uuid

from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.UUID, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'name'],
                condition=models.Q(is_deleted=False),
                name='unique_active_category_per_user'
            )
        ]
        
    def __str__(self):
        return f"{ self.user.username }: { self.name }"
        
        
        
        
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.UUID, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)
    deadline = models.DateField(blank=True, null=True)
    
    is_completed = models.BooleanField(default=False)
    
    @property
    def progress(self):
        total = self.subtasks.count()
        if total == 0:
            return 0.0
        completed = self.subtasks.filter(is_completed=True).count()
        return round((completed / total) * 100, 2)
        
    def __str__(self):
        return f"{ self.category.name }: { self.title }"
    
    
    
class Subtask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.UUID, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_subtasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{ self.task.title }: { self.title }"