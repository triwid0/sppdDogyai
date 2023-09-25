from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'sppd'
urlpatterns = [
    path('', dashboard.index, name='index'),
    path('master_tahun/', tahun.index, name='tahun'),
    path('master_tahun/tambah/', tahun.create, name='tambah'),
    path('hapus/<int:id>', tahun.permanentDelete, name='hapus'),
    path('master_tahun/edit/<int:id>', tahun.edit, name='edit'),
    path('master_tahun/off/<int:id>', tahun.Off, name='Off'),
    path('master_tahun/on/<int:id>', tahun.On, name='On'),
    # path('', app.task_list, name='task_list'),
    # path('create/', app.task_create, name='task_create'),
    # path('update/<int:pk>/', app.task_update, name='task_update'),
    # path('delete/<int:pk>/', app.task_delete, name='task_delete'),
]