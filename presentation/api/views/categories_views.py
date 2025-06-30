from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from infraestructure.repositories.category_repository_impl import DjangoCategoryRepository
from apps.tasks.models import Category
from use_cases import CreateCategoryUseCase, ListAllCategoriesUseCase, UpdateCategoryUseCase, DeleteCategoryUseCase

from ..serializers.category_serializer import CategoryDDESerializer, CategoryUpdateSerializer, CreateCategory


category_repo = DjangoCategoryRepository()

class CategoryCreateView(APIView):
    
    
    
    def post(self, request):
        serializer = CreateCategory(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_id = request.user.id
        validated = serializer.validated_data
        use_case = CreateCategoryUseCase(category_repo)
        
        
        # Se verifica duplicidad de nombre para category por usuario
        if Category.objects.filter(user_id=user_id, name=serializer.validated_data["name"], is_deleted=False).exists():
            return Response({"error": "Ya existe una categoría con ese nombre."}, status=status.HTTP_400_BAD_REQUEST)
        
        category = use_case.execute(
            name=validated.get("name"),
            user_id=user_id
        )
        
        if category:
            return Response({
                "id": str(category.id),
                "name": category.name
            }, status=status.HTTP_201_CREATED)
            
        return Response({
            "message": "Falló la creación de la categoría"
        }, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class ListCategoriesApiView(APIView):

    
    def get(self, request):
        
        user_id = request.user.id
        
        use_case = ListAllCategoriesUseCase(category_repo)
        
        categories = use_case.execute(user_id)
        
        if categories:
            serializer = CategoryDDESerializer(categories, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
            
        return Response([], status=status.HTTP_200_OK)
    
    
class UpdteCategoryApiView(APIView):
    
    def put(self, request, category_id):
        
        user_id = request.user.id
        
        serializer = CategoryUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        validated = serializer.validated_data
        name = validated.get("name")
        
        use_case = UpdateCategoryUseCase(category_repo)
        
        
        
        updated = use_case.execute(category_id, name, user_id)
        
        if updated:
            return Response({
                "message": "Categoria actualizada"
            }, status=status.HTTP_200_OK)
        
        return Response({
            "messasge": "no se pudo actualizar la categría"
        }, status=status.HTTP_400_BAD_REQUEST) 
        
        
        
class DeleteCategoryApiView(APIView):
    
    def put(self, request, category_id):
        
        user_id = request.user.id
        
        use_case = DeleteCategoryUseCase(category_repo)
       
        is_deleted = use_case.execute(category_id, user_id)
       
        if is_deleted:
                return Response({
                    "message": "Categoria eliminada"
                }, status=status.HTTP_200_OK)
            
        return Response({
            "messasge": "no se pudo eliminar la categría"
        }, status=status.HTTP_400_BAD_REQUEST) 