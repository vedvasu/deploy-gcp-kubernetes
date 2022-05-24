from django.db import models
from django.utils import timezone


class GeneratedText(models.Model):

    created_at = models.DateTimeField(default=timezone.now)

    input_text = models.TextField()
    generated_text_1 = models.TextField(default='')
    generated_text_2 = models.TextField(default='')
    generated_text_3 = models.TextField(default='')

    prediction_time_sec = models.IntegerField(default=0)
