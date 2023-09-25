from django.db import models
from django.utils import timezone
import datetime
from datetime import datetime
# Create your models here.



class MasterTahun(models.Model):
    tahun = models.CharField(max_length=4)
    status = models.BooleanField(max_length=1, default=False)

class MasterJabatan(models.Model):
    jabatan = models.CharField(max_length=225)
    status = models.BooleanField(max_length=1, default=False)