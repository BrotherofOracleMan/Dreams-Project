from django.db import models

# Create your models here.

class Dream(models.Model):
    id = models.TextField(primary_key=True)
    date = models.TextField(max_length=15)
    quote = models.TextField()