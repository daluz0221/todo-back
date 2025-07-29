from django.urls import path
from ...views.tasks_view import CreateTaskApiView, ListTasksApiView, UpdateTaskApiView, DeleteTaskApiView, GetTaskApiView


app_name = 'tasks_api'


urlpatterns = [
    path('', CreateTaskApiView.as_view(), name='create_task'), #POST
    path('list/', ListTasksApiView.as_view(), name='list_tasks'),
    path('list/<uuid:task_id>', GetTaskApiView.as_view(), name='get_task_by_id'),
    path('update/<uuid:task_id>', UpdateTaskApiView.as_view(), name='update_task'), # PUT
    path('delete/<uuid:task_id>', DeleteTaskApiView.as_view(), name='delete_task'), # PUT
]