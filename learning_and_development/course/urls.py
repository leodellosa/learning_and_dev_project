from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<str:title>/', views.course_detail, name='course_detail'),
    path('create/', views.course_create, name='course_create'),
    path('update/<int:id>/', views.course_update, name='course_update'),
]

