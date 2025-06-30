from rest_framework import serializers
from apps.tasks.models import Task

from .subtask_serializers import SubtaskSerializer
from .category_serializer import NestedCategorySerializer

class TaskSerializer(serializers.ModelSerializer):
    progress = serializers.FloatField(read_only=True)  # usa el @property

    class Meta:
        model = Task
        fields = [
            'id',
            'category',
            'title',
            'description',
            'is_completed',
            'deadline',
            'progress',
        ]
        read_only_fields = ['id', 'progress']


class TaskDetailSerializer(serializers.ModelSerializer):
    progress = serializers.FloatField(read_only=True)
    subtasks = SubtaskSerializer(many=True, read_only=True)
    category = NestedCategorySerializer(read_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'category',
            'title',
            'description',
            'is_completed',
            'deadline',
            'progress',
            'subtasks',
            'category'
        ]
        read_only_fields = ['id', 'progress', 'subtasks', 'category']