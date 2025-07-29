from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.tasks.models import Task
from infraestructure.repositories.task_repository_impl import DjangoTaskRepository
from use_cases import CreateTaskUseCase, ListAllTasksUseCase, UpdateTaskUseCase, DeleteTaskUseCase, GetTaskUseCase
from ..serializers import TaskCreateSerializer, TaskReadSerializer, TaskUpdateSerializer, TaskWithSubTasksDTOSerializer



task_repo = DjangoTaskRepository()


class CreateTaskApiView(APIView):
    
    def post(self, request):
        serializer = TaskCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_id = request.user.id
        validated = serializer.validated_data
        
        use_case = CreateTaskUseCase(task_repo)
        
        if Task.objects.filter(user_id=user_id, title=validated.get("title"), is_deleted=False).exists():
            return Response({
                "error": "Ya existe una tarea con ese título"
            }, status=status.HTTP_400_BAD_REQUEST)
            

        task = use_case.execute(
            title=validated.get("title"),
            description=validated.get("description"),
            deadline=validated.get("deadline"),
            category_id=validated.get("category_id"),
            user_id=user_id
        )
        
        
        if task:
            return Response({
                "message": "Tarea creada con éxito"
            }, status=status.HTTP_201_CREATED)    
    
        return Response({
            "message": "Falló la creación de la tarea"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class ListTasksApiView(APIView):
    
    def get(self, request):
        
        user_id = request.user.id
        use_case = ListAllTasksUseCase(task_repo)
        
        all_tasks = use_case.execute(user_id)
        
        if all_tasks:
            serializer = TaskReadSerializer(all_tasks, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
            
        return Response([], status=status.HTTP_200_OK)
        
   
class GetTaskApiView(APIView):
    
    def get(self, request, task_id):
        user_id = request.user.id
        
        use_case = GetTaskUseCase(task_repo)
        
        task = use_case.execute(task_id, user_id)
        
        if task:
            serializer = TaskWithSubTasksDTOSerializer(task)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        
        return Response({"message": "Falló la obtención de la información relacionada a la tarea"}, status=status.HTTP_400_BAD_REQUEST)

class UpdateTaskApiView(APIView):
    
    def put(self, request, task_id):
        
        user_id = request.user.id
        
        serializer = TaskUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            print("============================")
            print("llego")
            print("============================")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        validated = serializer.validated_data
        use_case = UpdateTaskUseCase(task_repo)

        updated_task = use_case.execute(
            task_id=task_id,
            title=validated.get("title"),
            description=validated.get("description"),
            dificulties=validated.get("dificulties"),
            solution=validated.get("solution"),
            is_completed=validated.get("is_completed"),
            deadline=validated.get("deadline"),
            category_id=validated.get("category_id"),
            user_id=user_id,
            
        )
        
        if updated_task:
            return Response({
                "message": "Tarea actualizada"
            }, status=status.HTTP_200_OK)
        
        return Response({
            "messasge": "no se pudo actualizar la Tarea"
        }, status=status.HTTP_400_BAD_REQUEST) 
        
        
 
class DeleteTaskApiView(APIView):
    
    def put(self, request, task_id):
        user_id = request.user.id
        
        use_case = DeleteTaskUseCase(task_repo)
        
        is_deleted = use_case.execute(task_id, user_id)
        
        if is_deleted:
            return Response({
                "message": "Tarea eliminada"
            }, status=status.HTTP_200_OK)
    
        return Response({
            "messasge": "no se pudo eliminar la tarea"
        }, status=status.HTTP_400_BAD_REQUEST) 
        
        
        
