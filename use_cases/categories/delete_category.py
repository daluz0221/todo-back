
from domain.entities.category import Category
from domain.repositories.category_repository import CategoryRepository
from uuid import UUID


class DeleteCategoryUseCase:
    
    def __init__(self, category_repo:CategoryRepository):
        self.category_repo = category_repo
        
        
    def execute(self, category_id: UUID,  user_id: UUID):
        
        
        is_deleted = self.category_repo.delete_category(category_id, user_id)
        if is_deleted:
            return True
        return False