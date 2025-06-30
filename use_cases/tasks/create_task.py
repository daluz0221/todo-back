from datetime import datetime
from domain.entities.task import Task
from domain.repositories.task_repository import TaskRepository
from uuid import UUID


class CreateTaskUseCase:
    
    def __init__(self, task_repo:TaskRepository):
        self.task_repo = task_repo
        
        
    def execute(self, title:str, description: str, deadline: datetime, category_id: UUID, user_id: UUID):
        task = Task(
            title=title,
            description=description,
            is_completed=False,
            is_deleted=False,
            deadline=deadline,
            category_id=category_id,
            user_id=user_id
        )
        
        is_created = self.task_repo.createTask(task)
        if is_created:
            return task
        return False