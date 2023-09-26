from django import forms
from ..models import *



class MasterTahun(forms.ModelForm):
	class Meta:
		model = MasterTahun
		fields = ('tahun',)

class MasterLokasi(forms.ModelForm):  
	class Meta:
		model = MasterLokasi
		fields = ('kd_lokasi',)
		fields = ('urai',)

class MasterJabatan(forms.ModelForm):
	class Meta:
		model = MasterJabatan
		fields = ('jabatan',)

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

