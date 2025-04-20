from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_table, name='create_table'),
    path('edit/<int:table_id>/', views.edit_table, name='edit_table'),
    path('view/<int:table_id>/', views.view_table, name='view_table'),
    path('delete/<int:table_id>/', views.delete_table, name='delete_table'),
]