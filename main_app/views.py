from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from .models import SigOther

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def relationships_index(request):
    relationships = SigOther.objects.all()
    return render(request, 'relationships/index.html', { 'relationships': relationships })

def relationships_detail(request, relationship_id):
  relationship = SigOther.objects.get(id=relationship_id)
  return render(request, 'relationships/detail.html', { 'relationship': relationship })

class RelationshipCreate(CreateView):
  model = SigOther
  fields = '__all__'
  success_url = '/relationships/'

class RelationshipUpdate(UpdateView):
  model = SigOther
  fields = '__all__'

class RelationshipDelete(DeleteView):
  model = SigOther
  success_url = '/relationships/'

