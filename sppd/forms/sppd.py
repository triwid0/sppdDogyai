from django import forms
from ..models import *



class MasterTahun(forms.ModelForm):
	class Meta:
		model = MasterTahun
		fields = ('tahun',)

<<<<<<< HEAD
class MasterTahun(forms.ModelForm):
	class Meta:
		model = MasterLokasi
		fields = ('kd_lokasi',)
		fields = ('urai',)
=======

class MasterJabatan(forms.ModelForm):
	class Meta:
		model = MasterJabatan
		fields = ('jabatan',)
>>>>>>> dab51d3061e792ba290ebc3ffd7cdec7fd7758b7
