from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:id>/', views.user_detail, name='user_detail'),
]

