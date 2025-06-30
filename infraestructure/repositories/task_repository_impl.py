

from domain.entities.task import Task
from domain.repositories.task_repository import TaskRepository

from apps.tasks.models import Task as TaskORM

from infraestructure.mappers.task_mapper import orm_to_entity, entity_to_orm




class DjangoTaskRepository(TaskRepository):
    
    
    def get_by_id(self, task_id):
        
        try:
            task = TaskORM.objects.get(id=task_id)
            return orm_to_entity(task)
        except:
            raise ValueError("Task not found")
        
    def get_all_tasks(self, user_id):
        
        all_users_tasks = TaskORM.objects.filter(user_id=user_id)
        return [ orm_to_entity(task) for task in all_users_tasks ]
    
    
    def list_by_category(self, category_id):
        tasks_by_cat = TaskORM.objects.filter(category_id=category_id)
        return [orm_to_entity(task) for task in tasks_by_cat]
    
    
    def createTask(self, task):
        try:
            TaskORM.objects.create(
                id=task.id,
                title=task.title,
                description=task.description,
                is_completed=task.is_completed,
                deadline=task.deadline,
                category_id=task.category_id,
                user_id=task.user_id
            )
            return True
        except:
            return False
        
    
    def update_task(self, task):
        
        try:
            task_orm = TaskORM.objects.get(id=task.id)
            task_orm.title = task.title
            task_orm.description = task.description
            task_orm.deadline = task.deadline
            task_orm.is_completed = task.is_completed
            task_orm.category = task.category_id
            task_orm.user = task.user_id
            task_orm.save()
            return True
        except TaskORM.DoesNotExist:
            return False
   
   
    def delete_task(self, task_id):
        
        try:
            task_orm = TaskORM.objects.get(id=task_id)
            task_orm.is_deleted = True
            task_orm.save()
            return True
        except TaskORM.DoesNotExist:
            return False