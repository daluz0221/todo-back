from django.contrib import admin
from .models import Category, Task, Subtask

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'is_deleted', 'created_at', 'last_updated')
    search_fields = ('name', 'user__username')
    list_filter = ('is_deleted', 'user')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'user', 'is_completed', 'deadline', 'is_deleted')
    search_fields = ('title', 'category__name', 'user__username')
    list_filter = ('is_completed', 'is_deleted', 'category', 'user')
    ordering = ('-deadline',)
    
@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'user', 'is_completed')
    search_fields = ('title', 'task__title', 'user__username')
    list_filter = ('is_completed', 'task', 'user')
    ordering = ('-task__deadline',)
    

# Register your models here.
