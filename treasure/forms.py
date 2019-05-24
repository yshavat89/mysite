from django import forms
from .models import Treasure

class TreasureForm(forms.ModelForm):

    class Meta:
        model = Treasure
        fields = ['name','value','material','location','image']
