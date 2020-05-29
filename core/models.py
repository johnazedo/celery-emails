from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.text


class Email(models.Model):
    text = models.EmailField()

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.text
