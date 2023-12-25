from django.urls import path
from .views import create_guest, show_guset, update_guest, delete_guest

urlpatterns = [
    path('create_guest/', create_guest),
    path('show_guest/', show_guset),
    path('update_guest/<int:pk>/', update_guest),
    path('delete_guest/<int:pk>/', delete_guest),

]