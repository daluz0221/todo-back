from rest_framework import serializers

from .subtask_serializers import SubTaskReadSerializer


class TaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    dificulties = serializers.CharField(required=False)
    solution = serializers.CharField(required=False)
    is_completed = serializers.BooleanField(default=False)
    is_deleted = serializers.BooleanField(default=False)
    deadline = serializers.DateTimeField()
    category_id = serializers.UUIDField()



class TaskUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    dificulties = serializers.CharField(required=False, allow_blank=True)
    solution = serializers.CharField(required=False, allow_blank=True)
    is_completed = serializers.BooleanField(required=False)
    deadline = serializers.DateTimeField(required=False)
    category_id = serializers.UUIDField(required=False)
    

class TaskReadSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    description = serializers.CharField()
    dificulties = serializers.CharField(required=False)
    solution = serializers.CharField(required=False)
    is_completed = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    deadline = serializers.DateTimeField()
    category_id = serializers.UUIDField()
    progress = serializers.FloatField()
    
    
class TaskWithSubTasksDTOSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    description = serializers.CharField()
    dificulties = serializers.CharField(required=False)
    solution = serializers.CharField(required=False)
    is_completed = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    deadline = serializers.DateTimeField()
    category_id = serializers.UUIDField()
    progress = serializers.FloatField()
    subtasks = SubTaskReadSerializer(many=True)