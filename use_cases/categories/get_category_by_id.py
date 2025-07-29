
from domain.entities.category import Category
from domain.repositories.category_repository import CategoryRepository
from uuid import UUID


class GetCategoryUseCase:
    
    def __init__(self, category_repo:CategoryRepository):
        self.category_repo = category_repo
        
        
    def execute(self, category_id: UUID, user_id: UUID):
        
        
        category = self.category_repo.get_by_id(category_id, user_id)
        if category:
            return category
        return False