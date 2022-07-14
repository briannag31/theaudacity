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
path('relationships/<int:relationship_id>/add_meeting/', views.add_meeting, name='add_meeting'),
path('traits/', views.TraitList.as_view(), name='traits_index'),
path('traits/<int:pk>/', views.TraitDetail.as_view(), name='traits_detail'),
path('traits/create/', views.TraitCreate.as_view(), name='traits_create'),
path('traits/<int:pk>/update/', views.TraitUpdate.as_view(), name='traits_update'),
path('traits/<int:pk>/delete/', views.TraitDelete.as_view(), name='traits_delete'),
path('relationships/<int:relationship_id>/assoc_trait/<int:trait_id>/', views.assoc_trait, name='assoc_trait'),

]