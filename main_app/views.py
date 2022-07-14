
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import SigOther, Trait
from .forms import MeetingsForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def relationships_index(request):
    relationships = SigOther.objects.all()
    return render(request, 'relationships/index.html', { 'relationships': relationships })

def relationships_detail(request, relationship_id):
  relationship = SigOther.objects.get(id=relationship_id)
  traits_sigother_doesnt_have = Trait.objects.exclude(id__in = relationship.traits.all().values_list('id'))
  meetings_form = MeetingsForm()
  return render(request, 'relationships/detail.html', { 'relationship': relationship, "meetings_form": meetings_form, "traits": traits_sigother_doesnt_have })

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

def add_meeting(request, relationship_id ):
  # create the ModelForm using the data in request.POST
  form = MeetingsForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_meeting = form.save(commit=False)
    new_meeting.relationship_id = relationship_id
    new_meeting.save()
  return redirect('detail', relationship_id=relationship_id)

def assoc_trait(request, relationship_id, trait_id):
  # Note that you can pass a toy's id instead of the whole object
  SigOther.objects.get(id=relationship_id).traits.add(trait_id)
  return redirect('detail', relationship_id=relationship_id)

class TraitList(ListView):
  model = Trait

class TraitDetail(DetailView):
  model = Trait

class TraitCreate(CreateView):
  model = Trait
  fields = ['name', 'designation']

class TraitUpdate(UpdateView):
  model = Trait
  fields = ['name', 'designation']

class TraitDelete(DeleteView):
  model = Trait
  success_url = '/traits/'

