from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

class Question(models.Model):
    author=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True ,related_name='author_question')
    question = models.CharField(max_length=350)
    tags =TaggableManager()
    created_at=models.DateTimeField(default=timezone.now)
    content=models.CharField(max_length=30)

class Answer(models.Model):
        author=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,related_name='author_answer')
        answer=models.TextField(max_length=2000)
        question = models.ForeignKey(Question,on_delete=models.SET_NULL,null=True,blank=True,related_name='question_answer')
        created_at=models.DateTimeField(default=timezone.now)
