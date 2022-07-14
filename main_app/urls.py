from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('relationships/', views.relationships_index, name='index'),
path('relationships/<int:relationship_id>/', views.relationships_detail, name='detail'),
]