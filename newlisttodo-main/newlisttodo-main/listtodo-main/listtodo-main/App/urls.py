from django.urls import path
from . import views

urlpatterns = [
    path('',views.newlisttodo,name='newlisttodo'),
    path('add_task',views.add_task,name='add_task'),
    path('delete_task/<int:task_id>',views.delete_task,name='delete_task'),
    path('newlisttodo',views.newlisttodo,name='newlisttodo'),
    path('edit_task/<int:task_id>/',views.edit_task,name='edit_task'),
    path('add_category',views.add_category,name='add_category')
    # path('baitho',views.baitho),
    # path('amduong/<str:a>',views.amDuong),
    # path('nhan/<str:a>',views.phepNhan)
]
