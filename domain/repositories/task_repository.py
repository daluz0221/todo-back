from abc import ABC, abstractmethod
from typing import List, Dict
from uuid import UUID
from domain.entities.task import Task


class TaskRepository(ABC):
    
    
    @abstractmethod
    def get_all_tasks(self, user_id: UUID) -> List[Task]:
        pass
    
    
    @abstractmethod
    def get_by_id(self, task_id: UUID) -> Task:
        pass
    
    
    @abstractmethod
    def update_task(self, task: Task) -> bool:
        pass
    
    
    @abstractmethod
    def list_by_category(self, category_id: UUID) -> List[Task]:
        pass
    
    
    @abstractmethod
    def createTask(self, task: Task) -> bool:
        pass
    
    
    @abstractmethod
    def delete_task(self, task_id: UUID, user_id:UUID) -> bool:
        pass