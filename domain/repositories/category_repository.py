from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from domain.entities.category import Category


class CategoryRepository(ABC):
    
    
    @abstractmethod
    def get_all_categories(self, user_id: UUID) -> List[Category]:
        pass
    
    
    @abstractmethod
    def get_by_id(self, category_id: UUID, user_id: UUID) -> Category:
        pass
    
    
    @abstractmethod
    def update_category(self, category: Category) -> bool:
        pass
    
    
    @abstractmethod
    def createCategory(self, category: Category) -> bool:
        pass
    
    
    @abstractmethod
    def delete_category(self, category_id: UUID, user_id: UUID) -> bool:
        pass