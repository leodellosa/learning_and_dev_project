from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('create/', views.course_create, name='course_create'),
    path('update/<int:id>/', views.course_update, name='course_update'),
    path('<int:id>/', views.course_detail_by_id, name='course_detail_by_id'),
    
]

