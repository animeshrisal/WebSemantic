from django.db import models

class tweets(models.Model):
    tweets = models.CharField(max_length = 300)