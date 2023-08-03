from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

class Question(models.Model):
    question = models.CharField(max_length=350)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True ,related_name='author_question')
    content=models.TextField(max_length=300)
    tags =TaggableManager()
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
         return self.question

class Answer(models.Model):
        question = models.ForeignKey(Question,on_delete=models.SET_NULL,null=True,blank=True,related_name='question_answer')
        answer=models.TextField(max_length=2000)
        author=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,related_name='author_answer')
        created_at=models.DateTimeField(default=timezone.now)
        def __str__(self):
            return self.answer
        
