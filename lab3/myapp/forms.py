from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from multiselectfield import MultiSelectFormField
from . import models


useer  =User.objects.all().values_list('username', flat=True)
choice = tuple((str(useer[i]), str(useer[i])) for i in range(len(useer)))

class EntryForm(forms.Form):
    name = forms.CharField(max_length=100)
    date = forms.DateTimeField()
    description = forms.CharField(widget=forms.Textarea)
    participants = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=choice)


