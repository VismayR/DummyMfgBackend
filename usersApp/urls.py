from django.urls import path
from .views import *

urlpatterns = [
    path('user',UserList.as_view()),
    path('user/<int:pk>', UserList.as_view()),
]