from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.timesheet_detail, name='timesheet_detail'),
]