from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('task-list/',views.get_all_task, name="task-list"),
    path('task-detail/<str:id>/',views.get_task_by_id, name="task-detail"),
    path('task-create/',views.create_task, name="task-create"),
    path('task-update/<str:id>/',views.update_task_by_id, name="task-update"),
    path('task-delete/<str:id>/',views.delete_task, name="task-delete"),
]