from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return  Question.objects.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    author = models.OneToOneField(User)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, blank=True)
    question = models.ForeignKey(Question)
    author = models.OneToOneField(User)
