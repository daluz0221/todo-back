from rest_framework import serializers
from apps.tasks.models import Subtask

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'title', 'description', 'is_completed']
        read_only_fields = ['id']