from rest_framework import serializers

class SubTaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    dificulties = serializers.CharField(required=False)
    solution = serializers.CharField(required=False)
    is_completed = serializers.BooleanField(default=False)
    is_deleted = serializers.BooleanField(default=False)
    task_id = serializers.UUIDField()
    
    
class SubTaskUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    dificulties = serializers.CharField(required=False)
    solution = serializers.CharField(required=False)
    is_completed = serializers.BooleanField(required=False)
    task_id = serializers.UUIDField()
    
    
class SubTaskReadSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    description = serializers.CharField()
    dificulties = serializers.CharField(required=False)
    solution = serializers.CharField(required=False)
    is_completed = serializers.BooleanField()
    task_id = serializers.UUIDField()