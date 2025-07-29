from django.urls import path

from ...views.subtasks_view import CreateSubTaskApiView, UpdateSubTaskApiView, DeleteSubTaskApiView, ListSubTasksApiView

app_name = 'subtasks_api'

urlpatterns = [
    path('', CreateSubTaskApiView.as_view(), name='create_subtask'), #POST
    path('list/', ListSubTasksApiView.as_view(), name='list_subtasks'),
    # path('list/<uuid:subtask_id>', ListSubTasksApiView.as_view(), name='list_subtasks'),
    path('update/<uuid:subtask_id>', UpdateSubTaskApiView.as_view(), name='update_subtask'), # PUT
    path('delete/<uuid:subtask_id>', DeleteSubTaskApiView.as_view(), name='delete_subtask'), # PUT
]