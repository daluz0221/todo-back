from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.tasks.models import Subtask
from infraestructure.repositories.subtask_repository_impl import DjangoSubTaskRepository
from use_cases import CreateSubTaskUseCase, ListAllSubTasksUseCase, UpdateSubTaskUseCase, DeleteSubTaskUseCase
from ..serializers import SubTaskUpdateSerializer, SubTaskReadSerializer, SubTaskCreateSerializer



subtask_repo = DjangoSubTaskRepository()


class CreateSubTaskApiView(APIView):
    
    def post(self, request):
        serializer = SubTaskCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_id = request.user.id
        validated = serializer.validated_data
        
        use_case = CreateSubTaskUseCase(subtask_repo)
        
        if Subtask.objects.filter(user_id=user_id, title=validated.get("title"), is_deleted=False).exists():
            return Response({
                "error": "Ya existe una subtarea con ese título"
            }, status=status.HTTP_400_BAD_REQUEST)
            

        subtask = use_case.execute(
            title=validated.get("title"),
            description=validated.get("description"),
            task_id=validated.get("task_id"),
            user_id=user_id
        )
        
        
        if subtask:
            return Response({
                "message": "Sub tarea creada con éxito"
            }, status=status.HTTP_201_CREATED)    
    
        return Response({
            "message": "Falló la creación de la sub tarea"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class ListSubTasksApiView(APIView):
    
    def get(self, request):
        
        user_id = request.user.id
        use_case = ListAllSubTasksUseCase(subtask_repo)
        
        all_subtasks = use_case.execute(user_id)
        
        if all_subtasks:
            serializer = SubTaskReadSerializer(all_subtasks, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
            
        return Response([], status=status.HTTP_200_OK)
        
        

class UpdateSubTaskApiView(APIView):
    
    def put(self, request, subtask_id):
        
        user_id = request.user.id
        
        serializer = SubTaskUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        validated = serializer.validated_data
        use_case = UpdateSubTaskUseCase(subtask_repo)


        updated_subtask = use_case.execute(
            subtask_id=subtask_id,
            title=validated.get("title"),
            description=validated.get("description"),
            is_completed=validated.get("is_completed"),
            task_id=validated.get("task_id"),
            user_id=user_id,
            
        )
        
        if updated_subtask:
            return Response({
                "message": "Subtarea actualizada"
            }, status=status.HTTP_200_OK)
        
        return Response({
            "messasge": "no se pudo actualizar la subtarea"
        }, status=status.HTTP_400_BAD_REQUEST) 
        
        
 
class DeleteSubTaskApiView(APIView):
    
    def put(self, request, subtask_id):
        user_id = request.user.id
        
        use_case = DeleteSubTaskUseCase(subtask_repo)
        
        is_deleted = use_case.execute(subtask_id, user_id)
        
        if is_deleted:
            return Response({
                "message": "Subtarea eliminada"
            }, status=status.HTTP_200_OK)
    
        return Response({
            "messasge": "no se pudo eliminar la subtarea"
        }, status=status.HTTP_400_BAD_REQUEST) 
        
        
        
