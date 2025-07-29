from domain.entities.category import Category
from domain.entities.task import Task

from domain.dtos.category_with_task_dto import CategoryWithTasksDTO
from apps.tasks.models import Category as CategoryORM, Task as TaskORM


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
    
    
def category_with_tasks_orm_to_dto(category_orm:CategoryORM) -> CategoryWithTasksDTO:
    tasks = []
    for task in getattr(category_orm, 'category_tasks', []):
        tasks.append(Task(
            id=task.id,
            title=task.title,
            description=task.description,
            is_completed=task.is_completed,
            is_deleted=task.is_deleted,
            deadline=task.deadline,
            user_id=task.user_id,
            category_id=task.category_id
        ))
        
    return CategoryWithTasksDTO(
         id=category_orm.id,
        name=category_orm.name,
        user_id=category_orm.user_id,
        is_deleted=category_orm.is_deleted,
        created_at=category_orm.created_at,
        last_updated=category_orm.last_updated,
        tasks=tasks
    )