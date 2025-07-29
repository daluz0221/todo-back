

from domain.repositories.subtask_repository import SubTaskRepository
from uuid import UUID


class ListAllSubTasksUseCase:
    
    def __init__(self, subtask_repo:SubTaskRepository):
        self.subtask_repo = subtask_repo
        
        
    def execute(self, user_id: UUID):
        
        
        all_subtasks = self.subtask_repo.get_all_subtasks(user_id)
        if len(all_subtasks) > 0:
            return all_subtasks
        return False