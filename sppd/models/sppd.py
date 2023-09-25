from django.db import models
from django.utils import timezone
import datetime
from datetime import datetime
# Create your models here.



class MasterTahun(models.Model):
    tahun = models.CharField(max_length=4)
    status = models.BooleanField(max_length=1, default=False)

<<<<<<< HEAD
class MasterLokasi(models.Model):
    kd_lokasi = models.CharField(max_length=225)
    urai = models.TextField(max_length=225)
=======
class MasterJabatan(models.Model):
    jabatan = models.CharField(max_length=225)
    status = models.BooleanField(max_length=1, default=False)
>>>>>>> dab51d3061e792ba290ebc3ffd7cdec7fd7758b7
