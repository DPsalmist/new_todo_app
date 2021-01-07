from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='list'),
	path('update/<int:pk>/', views.UpdateTask, name='update'),
	path('delete/<int:pk>/', views.DeleteTask, name='delete'),
]