from django import forms
from .models import TrialBalanceFile

class TrialBalanceForm(forms.ModelForm):
    class Meta:
        model = TrialBalanceFile
        fields = ('document', )