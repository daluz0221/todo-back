from datetime import datetime
from domain.entities.category import Category
from domain.repositories.category_repository import CategoryRepository
from uuid import UUID


class CreateCategoryUseCase:
    
    def __init__(self, category_repo:CategoryRepository):
        self.category_repo = category_repo
        
        
    def execute(self, name:str, user_id: UUID):
        category = Category(
            name=name,
            is_deleted=False,
            user_id=user_id
        )
        
        is_created = self.category_repo.createCategory(category)
        if is_created:
            return category
        return False