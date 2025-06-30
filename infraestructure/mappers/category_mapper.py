from domain.entities.category import Category
from apps.tasks.models import Category as CategoryORM


def orm_to_entity(category_orm: CategoryORM) -> Category:
    return Category(
        id=category_orm.id,
        name=category_orm.name,
        is_deleted=category_orm.is_deleted,
        user_id=category_orm.user_id
    )
    
    
def entity_to_orm(category_entity: Category) -> CategoryORM:
    return CategoryORM(
        id=category_entity.id,
        name=category_entity.name,
        is_deleted=category_entity.is_deleted,
        user_id=category_entity.user_id
    )