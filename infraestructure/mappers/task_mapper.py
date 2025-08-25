from domain.entities.task import Task
from domain.entities.subtask import Subtask
from apps.tasks.models import Task as TaskORM
from domain.dtos.task_with_subtask_dto import TaskWithSubTasksDTO


def orm_to_entity(task_orm: TaskORM) -> Task:
    return Task(
        id=task_orm.id,
        title=task_orm.title,
        description=task_orm.description,
        dificulties=task_orm.difficulties,
        solution=task_orm.solution,
        is_completed=task_orm.is_completed,
        is_deleted=task_orm.is_deleted,
        deadline=task_orm.deadline,
        category_id=task_orm.category_id,
        user_id=task_orm.user,
        progress=task_orm.progress
    )
    
    
def entity_to_orm(task_entity: Task) -> TaskORM:
    return TaskORM(
        id=task_entity.id,
        title=task_entity.title,
        description=task_entity.description,
        dificulties=task_entity.dificulties,
        solution=task_entity.solution,
        is_completed=task_entity.is_completed,
        is_deleted=task_entity.is_deleted,
        deadline=task_entity.deadline,
        category_id=task_entity.category_id,
        user_id=task_entity.user_id
    )

def task_with_subtasks_orm_to_dto(task_orm:TaskORM) -> TaskWithSubTasksDTO:
    subtasks = []
    for subtask in getattr(task_orm, "task_subtasks", []):
        print("====================")
        print("punto 2")
        print(subtask.id)
        # print(subtask.title)
        # print(subtask.description)
        print(subtask.difficulties)
        print(subtask.solution)
        print(subtask.is_completed)
        print(subtask.is_deleted)
        print(subtask.user_id)
        print(subtask.task_id)
        subtasks.append(Subtask(
            id=subtask.id,
            title=subtask.title,
            description=subtask.description,
            dificulties=subtask.difficulties,
            solution=subtask.solution,
            is_completed=subtask.is_completed,
            is_deleted=subtask.is_deleted,
            user_id=subtask.user_id,
            task_id=subtask.task_id
        ))
        print("====================")
        print("punto 3")
        print("====================")
    
    return TaskWithSubTasksDTO(
        id=task_orm.id,
        title=task_orm.title,
        description=task_orm.description,
        dificulties=task_orm.difficulties,
        solution=task_orm.solution,
        is_completed=task_orm.is_completed,
        deadline=task_orm.deadline,
        category_id=task_orm.category_id,
        user_id=task_orm.user,
        is_deleted=task_orm.is_deleted,
        progress=task_orm.progress,
        created_at=task_orm.created_at,
        last_updated=task_orm.last_updated,
        subtasks=subtasks
    )


# TODO: puede que esto fallé