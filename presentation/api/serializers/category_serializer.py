from rest_framework import serializers
from apps.tasks.models import Category

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