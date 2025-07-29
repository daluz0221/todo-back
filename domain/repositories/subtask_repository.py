from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from domain.entities.subtask import Subtask


class SubTaskRepository(ABC):
    
    
    @abstractmethod
    def get_all_subtasks(self, user_id: UUID) -> List[Subtask]:
        pass
    
    
    @abstractmethod
    def get_by_id(self, subtask_id: UUID) -> Subtask:
        pass
    
    
    @abstractmethod
    def update_subtask(self, subtask: Subtask) -> bool:
        pass
    
    
    @abstractmethod
    def create_sub_task(self, subtask: Subtask) -> bool:
        pass
    
    
    @abstractmethod
    def delete_subtask(self, subtask_id: UUID, user_id:UUID) -> bool:
        pass