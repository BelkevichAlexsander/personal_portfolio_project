from django.forms import ModelForm
from .models import Todoo

class TodooForm(ModelForm):
    class Meta:
        model = Todoo
        fields = ['title', 'memo', 'important']
