from datetime import datetime
from domain.entities.category import Category
from domain.repositories.category_repository import CategoryRepository
from uuid import UUID


class ListAllCategoriesUseCase:
    
    def __init__(self, category_repo:CategoryRepository):
        self.category_repo = category_repo
        
        
    def execute(self, user_id: UUID):
  
        
        all_categories = self.category_repo.get_all_categories(user_id)
        if all_categories:
            return all_categories
        return False