
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import SigOther, Trait, Photo
from .forms import MeetingsForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3


S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector-bg31'


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def relationships_index(request):
    relationships = SigOther.objects.filter(user=request.user)
    return render(request, 'relationships/index.html', { 'relationships': relationships })

@login_required
def relationships_detail(request, relationship_id):
  relationship = SigOther.objects.get(id=relationship_id)
  traits_sigother_doesnt_have = Trait.objects.exclude(id__in = relationship.traits.all().values_list('id'))
  meetings_form = MeetingsForm()
  return render(request, 'relationships/detail.html', { 'relationship': relationship, "meetings_form": meetings_form, "traits": traits_sigother_doesnt_have })

class RelationshipCreate(LoginRequiredMixin, CreateView):
  model = SigOther
  fields = ['name', "met", "description", "break_up"]
  success_url = '/relationships/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RelationshipUpdate(LoginRequiredMixin, UpdateView):
  model = SigOther
  fields = '__all__'

class RelationshipDelete(LoginRequiredMixin, DeleteView):
  model = SigOther
  success_url = '/relationships/'

@login_required
def add_meeting(request, relationship_id ):
  form = MeetingsForm(request.POST)
  if form.is_valid():
    new_meeting = form.save(commit=False)
    new_meeting.relationship_id = relationship_id
    new_meeting.save()
  return redirect('detail', relationship_id=relationship_id)

@login_required
def assoc_trait(request, relationship_id, trait_id):
  SigOther.objects.get(id=relationship_id).traits.add(trait_id)
  return redirect('detail', relationship_id=relationship_id)

class TraitList(LoginRequiredMixin, ListView):
  model = Trait

class TraitDetail(LoginRequiredMixin, DetailView):
  model = Trait

class TraitCreate(LoginRequiredMixin, CreateView):
  model = Trait
  fields = ['name']

class TraitUpdate(LoginRequiredMixin, UpdateView):
  model = Trait
  fields = ['name']

class TraitDelete(LoginRequiredMixin, DeleteView):
  model = Trait
  success_url = '/traits/'

@login_required
def add_photo(request, relationship_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, relationship_id=relationship_id)
            photo.save()
        except:
            print('An error occurred')
    return redirect('detail', relationship_id=relationship_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign-up - try again!'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)