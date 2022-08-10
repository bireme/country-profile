from django import forms
from django.forms import inlineformset_factory

from main.models import *

class IndicatorForm(forms.ModelForm):
    class Meta:
        model = CountryIndicator
        exclude = ('profile', 'indicator',) # hidden fields on the form


DataFormSet = inlineformset_factory(CountryIndicator, CountryIndicatorData, form=IndicatorForm, extra=1,
                                     can_delete=True)