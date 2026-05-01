from django import forms
from . import models
class userForm(forms.ModelForm):
    class Meta:
        model=models.User
        fields=['ism','familiya','yosh','picture']
        