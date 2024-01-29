from django import forms 
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'
