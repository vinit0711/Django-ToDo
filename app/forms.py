
from django import forms
from .models import TODO


class TODOForm(forms.ModelForm):
    class Meta():
        model =  TODO
        fields = ['task','status','priority']







