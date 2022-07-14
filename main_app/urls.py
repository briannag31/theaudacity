from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('relationships/', views.relationships_index, name='index'),
path('relationships/<int:relationship_id>/', views.relationships_detail, name='detail'),
path('relationships/create/', views.RelationshipCreate.as_view(), name='relationship_create'),
path('relationships/<int:pk>/update/', views.RelationshipUpdate.as_view(), name='relationship_update'),
path('relationships/<int:pk>/delete/', views.RelationshipDelete.as_view(), name='relationship_delete'),
]