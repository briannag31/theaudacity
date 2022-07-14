from django.db import models
from django.urls import reverse

class SigOther(models.Model):
    name = models.CharField(max_length=100)
    met = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    break_up = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sigother_id': self.id})