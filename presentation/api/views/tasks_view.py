from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from infraestructure.repositories.task_repository_impl import DjangoTaskRepository
from use_cases import CreateTaskUseCase, ListAllTasksUseCase
from ..serializers import TaskSerializer, TaskDetailSerializer



task_repo = DjangoTaskRepository()

class CreateTaskApiView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
    
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = request.user.id
        validated = serializer.validated_data
        
        # Inyección de dependencias
        
        use_case = CreateTaskUseCase(task_repo)
        
        task = use_case.execute(
            title=validated.get("title"),
            description=validated.get("description"),
            deadline=validated.get("deadline"),
            category_id=validated.get("category_id").id,
            user_id=user_id
        )
        
        if task:
            return Response({
                "id": str(task.id),
                "title": task.title,
                "description": task.description,
                "is_completed": task.is_completed,
                "deadline": task.deadline
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Falló la creación de la tarea"
        }, status=status.HTTP_400_BAD_REQUEST)
        
        
class ListTaskApiView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        user_id = request.user.id
        
        
        use_case = ListAllTasksUseCase(task_repo)
        
        tasks = use_case.execute(user_id)
        
        if tasks:
            pass