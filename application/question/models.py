from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    actor_id = models.CharField(max_length=255)
    actor_name = models.CharField(max_length=255)
    answerAvailable = models.CharField(max_length=255)
    isSaved = models.BooleanField(default=True)
    isVote = models.BooleanField(default=True)
    accepted = models.BooleanField(default=True)
    vote = models.IntegerField(default=0)
    createdAtDate = models.DateTimeField(auto_now_add=True)
    
