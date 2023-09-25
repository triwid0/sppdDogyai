from django import forms
from ..models import *



class MasterTahun(forms.ModelForm):
	class Meta:
		model = MasterTahun
		fields = ('tahun',)


class MasterTahun(forms.ModelForm):
	class Meta:
		model = MasterLokasi
		fields = ('kd_lokasi',)
		fields = ('urai',)

class MasterJabatan(forms.ModelForm):
	class Meta:
		model = MasterJabatan
		fields = ('jabatan',)

