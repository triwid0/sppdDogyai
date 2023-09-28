from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'sppd'
urlpatterns = [
    path('', login.loginUser, name='login'),
    path('adduser/', login.addUser, name='adduser'),
    path('dash/', dashboard.index, name='dash'),
    path('master_tahun/', tahun.index, name='tahun'),
    path('master_tahun/tambah/', tahun.create, name='tambah'),
    path('master_tahun/hapus/<int:id>', tahun.permanentDelete, name='hapus'),
    path('master_tahun/edit/<int:id>', tahun.edit, name='edit'),
    path('master_tahun/off/<int:id>', tahun.Off, name='Off'),
    path('master_tahun/on/<int:id>', tahun.On, name='On'),

    #master lokasi
    path('master_lokasi/', lokasi.index, name='lokasi'),
    path('master_lokasi/tambah/', lokasi.create, name='tambah'),
    path('master_lokasi/hapus/<int:id>', lokasi.permanentDelete, name='hapus'),  
    path('master_lokasi/edit/<int:id>', lokasi.edit, name='edit'),  

    # master_jabatan
    path('master_jabatan/', jabatan.index, name='jabatan'),
    path('master_jabatan/tambah/', jabatan.create, name='tambah'),
    path('master_jabatan/hapus/<int:id>', jabatan.permanentDelete, name='hapus'),
    path('master_jabatan/edit/<int:id>', jabatan.edit, name='edit'),
    path('master_jabatan/off/<int:id>', jabatan.Off, name='Off'),
    path('master_jabatan/on/<int:id>', jabatan.On, name='On'),
 
    # master_pegawai
    path('master_pegawai/', pegawai.index, name='pegawai'),
    path('master_pegawai/tambah/', pegawai.create, name='tambah'),
    path('master_pegawai/hapus/<int:id>', pegawai.permanentDelete, name='hapus'),  
    path('master_pegawai/edit/<int:id>', pegawai.edit, name='edit'), 


    # pengesah
    path('master_pengesah/', pengesah.index, name='pengesah'),
    path('master_pengesah/tambah/', pengesah.create, name='tambah'),
    path('master_pengesah/hapus/<int:id>', pengesah.permanentDelete, name='hapus'),  
    path('master_pengesah/edit/<int:id>', pengesah.edit, name='edit'),
    path('master_pengesah/off/<int:id>', pengesah.Off, name='Off'),
    path('master_pengesah/on/<int:id>', pengesah.On, name='On'),
    
    # master_organisasi
    path('master_organisasi/', organisasi.index, name='organisasi'),
    path('master_organisasi/tambah/', organisasi.create, name='tambah'),
    path('master_organisasi/edit/<int:id>', organisasi.edit, name='edit'),
    path('master_organisasi/hapus/<int:id>', organisasi.permanentDelete, name='hapus'),
    # path('master_jabatan/edit/<int:id>', jabatan.edit, name='edit'),
    # path('master_jabatan/off/<int:id>', jabatan.Off, name='Off'),
    # path('master_jabatan/on/<int:id>', jabatan.On, name='On'),
    

]