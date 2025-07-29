
from domain.entities.subtask import Subtask
from domain.repositories.subtask_repository import SubTaskRepository
from uuid import UUID


class UpdateSubTaskUseCase:
    
    def __init__(self, subtask_repo:SubTaskRepository):
        self.subtask_repo = subtask_repo
        
        
    def execute(self, subtask_id: UUID, title:str, description: str, is_completed: bool, task_id: UUID, user_id: UUID):
        subtask = Subtask(
            id=subtask_id,
            title=title,
            description=description,
            is_completed=is_completed,
            is_deleted=False,
            task_id=task_id,
            user_id=user_id
        )
        
        is_updated = self.subtask_repo.update_subtask(subtask)
        if is_updated:
            return True
        return False