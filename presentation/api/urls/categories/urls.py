from django.urls import path
from ...views.categories_views import CategoryCreateView, ListCategoriesApiView, UpdteCategoryApiView, DeleteCategoryApiView

app_name = 'categories_api'

urlpatterns = [
    path('', CategoryCreateView.as_view(), name='create_category'), #POST
    path('list/', ListCategoriesApiView.as_view(), name='list_categories'),
    path('update/<uuid:category_id>', UpdteCategoryApiView.as_view(), name='update_category'), # PUT
    path('delete/<uuid:category_id>', DeleteCategoryApiView.as_view(), name='delete_category'), # PATCH
]