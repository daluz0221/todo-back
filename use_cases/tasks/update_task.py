from datetime import datetime
from domain.entities.task import Task
from domain.repositories.task_repository import TaskRepository
from uuid import UUID


class UpdateTaskUseCase:
    
    def __init__(self, task_repo:TaskRepository):
        self.task_repo = task_repo
        
        
    def execute(self, task_id: UUID, title:str, description: str, dificulties: str, solution: str, is_completed: bool, deadline: datetime, category_id: UUID, user_id: UUID):
        task = Task(
            id=task_id,
            title=title,
            description=description,
            dificulties=dificulties,
            solution=solution,
            is_completed=is_completed,
            is_deleted=False,
            deadline=deadline,
            category_id=category_id,
            user_id=user_id
        )
        
        is_updated = self.task_repo.update_task(task)
        if is_updated:
            return True
        return False