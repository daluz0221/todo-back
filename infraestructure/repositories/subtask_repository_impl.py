

from domain.entities.subtask import Subtask
from domain.repositories.subtask_repository import SubTaskRepository

from apps.tasks.models import Subtask as SubTaskORM

from infraestructure.mappers.subtask_mapper import orm_to_entity, entity_to_orm




class DjangoSubTaskRepository(SubTaskRepository):
    
    
    def get_by_id(self, subtask_id):
        
        try:
            task = SubTaskORM.objects.get(id=subtask_id)
            return orm_to_entity(task)
        except:
            raise ValueError("Task not found")
        
    def get_all_subtasks(self, user_id):
        
        all_users_subtasks = SubTaskORM.objects.filter(user_id=user_id, is_deleted=False)
        return [ orm_to_entity(subtask) for subtask in all_users_subtasks ]
    
    
    def create_sub_task(self, subtask):
        try:
            SubTaskORM.objects.create(
                id=subtask.id,
                title=subtask.title,
                description=subtask.description,
                is_completed=subtask.is_completed,
                task_id=subtask.task_id,
                user_id=subtask.user_id
            )
            return True
        except:
            return False
        
    
    def update_subtask(self, subtask):
        
        try:
            subtask_orm = SubTaskORM.objects.get(id=subtask.id, task_id=subtask.task_id)
            subtask_orm.title = subtask.title
            subtask_orm.description = subtask.description
            subtask_orm.is_completed = subtask.is_completed
            subtask_orm.save()
            return True
        except SubTaskORM.DoesNotExist:
            return False
   
   
    def delete_subtask(self, subtask_id, user_id):
        
        try:
            subtask_orm = SubTaskORM.objects.get(id=subtask_id, user_id=user_id)
            subtask_orm.is_deleted = True
            subtask_orm.save()
            return True
        except SubTaskORM.DoesNotExist:
            return False