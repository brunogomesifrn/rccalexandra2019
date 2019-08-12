from django.forms import ModelForm
from .models import Areas

class AreasForm(ModelForm):
	class Meta():
		model = Areas
		fields = ['nome'] 