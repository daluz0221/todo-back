from domain.entities.task import Task
from apps.tasks.models import Task as TaskORM


def orm_to_entity(task_orm: TaskORM) -> Task:
    return Task(
        id=task_orm.id,
        title=task_orm.title,
        description=task_orm.description,
        is_completed=task_orm.is_completed,
        is_deleted=task_orm.is_deleted,
        deadline=task_orm.deadline,
        category_id=task_orm.category_id,
        user_id=task_orm.user
    )
    
    
def entity_to_orm(task_entity: Task) -> TaskORM:
    return TaskORM(
        id=task_entity.id,
        title=task_entity.title,
        description=task_entity.description,
        is_completed=task_entity.is_completed,
        is_deleted=task_entity.is_deleted,
        deadline=task_entity.deadline,
        category_id=task_entity.category_id,
        user_id=task_entity.user_id
    )
    
# TODO: puede que esto fallé