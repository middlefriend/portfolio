from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Todo(models.Model):
    #author = models.ForeignKey(User.username, on_delete=models.CASCADE, related_name='author_todo',null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_todo')
    title = models.CharField(max_length=200)
    description = models.TextField() 
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment',null=True)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    todo_id = models.ForeignKey(Todo, null=True, blank=True, on_delete=models.CASCADE, related_name='get_todoer_id')
