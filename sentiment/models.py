from django.db import models

class news(models.Model):
    newstitle = models.TextField()
    newsdescription = models.TextField()
    date = models.DateField()
    negative_value = models.DecimalField(max_digits = 6, decimal_places = 3)
    neutral_value = models.DecimalField(max_digits = 6, decimal_places = 3)
    positive = models.DecimalField(max_digits = 6, decimal_places = 3)