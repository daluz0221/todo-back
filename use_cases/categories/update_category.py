
from domain.entities.category import Category
from domain.repositories.category_repository import CategoryRepository
from uuid import UUID


class UpdateCategoryUseCase:
    
    def __init__(self, category_repo:CategoryRepository):
        self.category_repo = category_repo
        
        
    def execute(self, category_id: UUID, name:str, user_id: UUID):
        category = Category(
            id=category_id,
            name=name,
            is_deleted=False,
            user_id=user_id
        )
        
        is_updated = self.category_repo.update_category(category)
        if is_updated:
            return category
        return False