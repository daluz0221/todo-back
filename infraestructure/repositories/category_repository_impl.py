
from django.db.models import Prefetch


from domain.entities.category import Category
from domain.repositories.category_repository import CategoryRepository

from apps.tasks.models import Category as CategoryORM
from apps.tasks.models import Task as TaskORM

from infraestructure.mappers.category_mapper import orm_to_entity, entity_to_orm, category_with_tasks_orm_to_dto



class DjangoCategoryRepository(CategoryRepository):
    
    
    def get_by_id(self, category_id, user_id):
      
        try:
            # category = CategoryORM.objects.get(id=category_id, user_id=user_id)
            category = CategoryORM.objects.prefetch_related(
                Prefetch(
                    'tasks',
                    queryset=TaskORM.objects.filter(user_id=user_id, is_deleted=False),
                    to_attr="category_tasks"
                )
            ).get(id=category_id, user_id=user_id)
            
            return category_with_tasks_orm_to_dto(category)

        except:
            raise ValueError("Category not found")
        
    def get_all_categories(self, user_id):
        
        all_user_categories = CategoryORM.objects.filter(user_id=user_id, is_deleted=False)
        
        return [ orm_to_entity(category) for category in all_user_categories ]
    
    
    def createCategory(self, category):
        try:
            CategoryORM.objects.create(
                id=category.id,
                name=category.name,
                is_deleted=category.is_deleted,
                user_id=category.user_id
            )
            return True
        except:
            return False
        
    
    def update_category(self, category):
        
        try:
            category_orm = CategoryORM.objects.get(id=category.id, user_id=category.user_id)
            category_orm.name = category.name
            category_orm.save()
            return True
        except CategoryORM.DoesNotExist:
            return False
   
   
    def delete_category(self, category_id, user_id):
        
        try:
            category_orm = CategoryORM.objects.get(id=category_id, user_id=user_id)
            category_orm.is_deleted = True
            category_orm.save()
            return True
        except CategoryORM.DoesNotExist:
            return False