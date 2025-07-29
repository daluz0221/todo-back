from domain.entities.subtask import Subtask
from apps.tasks.models import Subtask as SubTaskORM


def orm_to_entity(subtask_orm: SubTaskORM) -> Subtask:
    return Subtask(
        id=subtask_orm.id,
        title=subtask_orm.title,
        description=subtask_orm.description,
        dificulties=subtask_orm.difficulties,
        solution=subtask_orm.solution,
        is_completed=subtask_orm.is_completed,
        is_deleted=subtask_orm.is_deleted,
        task_id=subtask_orm.task_id,
        user_id=subtask_orm.user,
    )
    
    
def entity_to_orm(subtask_entity: Subtask) -> SubTaskORM:
    return SubTaskORM(
        id=subtask_entity.id,
        title=subtask_entity.title,
        description=subtask_entity.description,
        dificulties=subtask_entity.dificulties,
        solution=subtask_entity.solution,
        is_completed=subtask_entity.is_completed,
        is_deleted=subtask_entity.is_deleted,
        task_id=subtask_entity.task_id,
        user_id=subtask_entity.user_id
    )
    
# TODO: puede que esto fallé