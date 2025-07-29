
from domain.repositories.task_repository import TaskRepository
from uuid import UUID


class GetTaskUseCase:
    
    def __init__(self, task_repo:TaskRepository):
        self.task_repo = task_repo
        
        
    def execute(self, task_id: UUID, user_id: UUID):
        
        
        task_by_id = self.task_repo.get_by_id(task_id, user_id)
        if task_by_id:
            return task_by_id
        return False