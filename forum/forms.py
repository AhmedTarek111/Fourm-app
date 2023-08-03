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

class Editquestion(forms.ModelForm):
    class Meta:
        model = Question
        fields =['question','content','tags']
class Editanswer(forms.ModelForm):
    class Meta:
        model =Answer
        fields=['answer',]