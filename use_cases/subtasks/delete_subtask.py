

from domain.repositories.subtask_repository import SubTaskRepository
from uuid import UUID


class DeleteSubTaskUseCase:
    
    def __init__(self, subtask_repo:SubTaskRepository):
        self.subtask_repo = subtask_repo
        
        
    def execute(self, subtask_id: UUID, user_id: UUID):
        
        is_deleted = self.subtask_repo.delete_subtask(subtask_id, user_id)
        if is_deleted:
            return True
        return False