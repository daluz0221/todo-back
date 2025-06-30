from rest_framework import serializers
from uuid import UUID, uuid4
from datetime import datetime

from domain.entities.task import Task

from .subtask_serializers import SubtaskSerializer
from .category_serializer import NestedCategorySerializer

class TaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    is_completed = serializers.BooleanField(default=False)
    is_deleted = serializers.BooleanField(default=False)
    deadline = serializers.DateTimeField()
    category_id = serializers.UUIDField()



class TaskUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    is_completed = serializers.BooleanField(required=False)
    deadline = serializers.DateTimeField(required=False)
    category_id = serializers.UUIDField(required=False)
    

class TaskReadSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    description = serializers.CharField()
    is_completed = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    deadline = serializers.DateTimeField()
    category_id = serializers.UUIDField()
    
    
