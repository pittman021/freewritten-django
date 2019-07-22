from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    content = models.TextField()
    word_count = models.IntegerField()
    pub_date = models.DateField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.content