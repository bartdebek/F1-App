from django import forms
from django.forms import formset_factory

from champions.models import SeasonResults

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class RaceForm(forms.ModelForm):
    class Meta:
        model = SeasonResults
        fields = '__all__'


class RaceFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = False
        self.template = 'bootstrap/table_inline_formset.html'
        self.add_input(Submit('submit', 'Save'))
        
    