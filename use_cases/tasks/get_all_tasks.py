from datetime import datetime
from domain.entities.task import Task
from domain.repositories.task_repository import TaskRepository
from uuid import UUID


class ListAllTasksUseCase:
    
    def __init__(self, task_repo:TaskRepository):
        self.task_repo = task_repo
        
        
    def execute(self, user_id: UUID):
        
        
        all_tasks = self.task_repo.get_all_tasks(user_id)
        if len(all_tasks) > 0:
            return all_tasks
        return False