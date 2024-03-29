from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    user = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    content = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
