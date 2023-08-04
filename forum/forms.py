from .models import *
from django import forms


class Questionform(forms.ModelForm):
    class Meta:
        model=Question
        exclude=('author',)

class Answerform(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['answer',]

