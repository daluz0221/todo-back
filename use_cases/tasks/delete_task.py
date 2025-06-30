from datetime import datetime
from domain.entities.task import Task
from domain.repositories.task_repository import TaskRepository
from uuid import UUID


class DeleteTaskUseCase:
    
    def __init__(self, task_repo:TaskRepository):
        self.task_repo = task_repo
        
        
    def execute(self, task_id: UUID, user_id: UUID):
        
        is_deleted = self.task_repo.delete_task(task_id, user_id)
        if is_deleted:
            return True
        return False