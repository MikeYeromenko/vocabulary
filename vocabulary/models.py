# from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Word(models.Model):
    english_word = models.CharField(max_length=150)
    russian_word = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.english_word} - {self.russian_word}'
