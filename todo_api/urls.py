from django.urls import path, include
# from django.conf.urls import url
from todo_api.views import (
    TodoListApiView,
    TodoDetailApiView,
)

urlpatterns = [
    path('api/', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
]
