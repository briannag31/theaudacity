from django.forms import ModelForm
from .models import Meetings

class MeetingsForm(ModelForm):
  class Meta:
    model = Meetings
    fields = ["date", "location", "rating", "details"]