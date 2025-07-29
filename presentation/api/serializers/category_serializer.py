from rest_framework import serializers
from apps.tasks.models import Category

from .task_serializers import TaskReadSerializer

class NestedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CreateCategory(serializers.Serializer):
    name = serializers.CharField()

class CategoryDDESerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    
    
class CategoryUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    
    
class CategoryWithTasksDTOSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    user_id = serializers.UUIDField()
    is_deleted = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    last_updated = serializers.DateTimeField()
    tasks = TaskReadSerializer(many=True)