from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Trait(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('traits_detail', kwargs={'pk': self.id})


class SigOther(models.Model):
    name = models.CharField(max_length=100)
    met = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    break_up = models.TextField(max_length=250)
    traits = models.ManyToManyField(Trait)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sigother_id': self.id})
    

class Meetings(models.Model):
  date = models.DateField()
  location = models.CharField(max_length=100)
  rating = models.IntegerField("Rating out of 10")
  details = models.TextField(max_length=250)

  relationship = models.ForeignKey(SigOther, on_delete=models.CASCADE)

  class Meta:
    ordering = ['-date']

  def __str__(self):
    return f" We met on {self.date} at {self.location}"

class Photo(models.Model):
    url = models.CharField(max_length=200)
    relationship = models.ForeignKey(SigOther, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for relationship_id: {self.relationship_id} @{self.url}"
