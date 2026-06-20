from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('tasks/', views.task_list, name='task_list'),
    path("create/", views.task_create, name="task_create"),
    path("update/<int:id>/", views.task_update, name="task_update"),
    path("delete/<int:id>/", views.task_delete, name="task_delete"),
]


