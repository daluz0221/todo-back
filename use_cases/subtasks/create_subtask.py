
from domain.entities.subtask import Subtask
from domain.repositories.subtask_repository import SubTaskRepository
from uuid import UUID


class CreateSubTaskUseCase:
    
    def __init__(self, subtask_repo:SubTaskRepository):
        self.subtask_repo = subtask_repo
        
        
    def execute(self, title:str, description: str, task_id: UUID, user_id: UUID):
        subtask = Subtask(
            title=title,
            description=description,
            is_completed=False,
            is_deleted=False,
            task_id=task_id,
            user_id=user_id
        )
        
        is_created = self.subtask_repo.create_sub_task(subtask)
        if is_created:
            return subtask
        return False