from django.db import models
from django.utils import timezone
import datetime
from datetime import datetime

# Create your models here.



class MasterTahun(models.Model):
    tahun = models.CharField(max_length=4)
    status = models.BooleanField(max_length=1, default=False)

class MasterLokasi(models.Model):
    kd_lokasi = models.CharField(max_length=225)
    urai = models.TextField(max_length=225)

class MasterJabatan(models.Model):
    jabatan = models.CharField(max_length=225)
    status = models.BooleanField(max_length=1, default=False)

class MasterPegawai(models.Model):
    nip = models.CharField(max_length=225)
    nama = models.CharField(max_length=225)
    golongan = models.CharField(max_length=225)
    no_hp = models.CharField(max_length=225)
    eselon = models.CharField(max_length=225)
    alamat = models.CharField(max_length=225)
    pangkat = models.TextField(max_length=225)
    email = models.TextField(max_length=225)
