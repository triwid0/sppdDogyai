from django import forms
from ..models import *



class MasterTahun(forms.ModelForm):
	class Meta:
		model = MasterTahun
		fields = ('tahun',)