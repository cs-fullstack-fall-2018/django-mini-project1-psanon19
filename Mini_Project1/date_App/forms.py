from django import forms
from .models import TimeSheet


class PostForm(forms.ModelForm):
    class Meta:
        model = TimeSheet
        fields = {'name', 'hours', }
