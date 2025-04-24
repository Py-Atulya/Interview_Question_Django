from django.db import models

class QuestionModel(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=100)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
