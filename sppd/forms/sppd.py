from django import forms
from ..models import *



class MasterTahun(forms.ModelForm):
	class Meta:
		model = MasterTahun
		fields = ('tahun',)


class Account(forms.ModelForm):
	class Meta:
		model = Account
		fields = ('nama','email', 'hak_akses', 'is_staff', 'is_active')

class MasterLokasi(forms.ModelForm):  
	class Meta:
		model = MasterLokasi
		fields = ('kd_lokasi',)
		fields = ('urai',)

class MasterJabatan(forms.ModelForm):
	class Meta:
		model = MasterJabatan
		fields = ('jabatan',)

class MasterPengesah(forms.ModelForm):
	class Meta:
		model = MasterPengesah
		fields = ('no_rek', 'nama_bank', 'status', 'pegawai', 'jabatan')

class MasterPegawai(forms.ModelForm):
	class Meta:
		model = MasterPegawai
		fields = ('nip',)
		fields = ('nama',)
		fields = ('golongan',)
		fields = ('eselon',)
		fields = ('pangkat',)
		fields = ('nohp',)
		fields = ('email',)
		fields = ('alamat',)

class MasterOrganisasi(forms.ModelForm):
	class Meta:
		model = MasterOrganisasi
		fields = ('id_organisasi',)
		fields = ('kode_organisasi',)
		fields = ('urai',)
