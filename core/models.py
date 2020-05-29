from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=1000)


class Email(models.Model):
    text = models.EmailField()