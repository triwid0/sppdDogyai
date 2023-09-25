from django import forms
from ..models import *



class MasterTahun(forms.ModelForm):
	class Meta:
		model = MasterTahun
		fields = ('tahun',)


class MasterJabatan(forms.ModelForm):
	class Meta:
		model = MasterJabatan
		fields = ('jabatan',)