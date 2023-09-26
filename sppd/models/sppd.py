
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class MasterOrganisasi(models.Model):
    id_organisasi = models.AutoField(primary_key=True)
    kode_organisasi = models.CharField(max_length=225, default='none')
    urai = models.CharField(max_length=225)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    id_user = models.AutoField(primary_key=True, default=False)
    id_organisasi = models.ForeignKey(MasterOrganisasi, on_delete=models.CASCADE, null=True, blank=True)
    nama = models.CharField(max_length=40)
    email = models.EmailField(_("email address"), unique=True)
    hak_akses = models.CharField(max_length=30, default="pegawai")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    groups = models.ManyToManyField(Group, related_name="user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="user_set", blank=True)

class MasterTahun(models.Model):
    tahun = models.CharField(max_length=4)
    status = models.BooleanField(default=False)

class MasterLokasi(models.Model):
    kd_lokasi = models.CharField(max_length=225)
    urai = models.TextField(max_length=225)

class MasterJabatan(models.Model):
    jabatan = models.CharField(max_length=225)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.jabatan

class MasterPegawai(models.Model):
    nip = models.CharField(max_length=225)
    nama = models.CharField(max_length=225)
    golongan = models.CharField(max_length=225)
    no_hp = models.CharField(max_length=225)
    eselon = models.CharField(max_length=225)
    alamat = models.CharField(max_length=225)
    pangkat = models.TextField(max_length=225)
    email = models.EmailField(max_length=225)

    def __str__(self):
        return self.nama

class MasterPengesah(models.Model):
    no_rek = models.TextField(max_length=225)
    nama_bank = models.TextField(max_length=225)
    status = models.BooleanField(default=False)
    jabatan = models.ForeignKey(MasterJabatan, on_delete=models.RESTRICT)
    pegawai = models.ForeignKey(MasterPegawai, on_delete=models.RESTRICT)

    def _jabatan_(self):
        return self.jabatan.jabatan

    def _pegawai_(self):
        return self.pegawai.nama

    def __str__(self):
        return f'(Pengesah: {self.pegawai.nama} ({self.jabatan.jabatan})'

        
