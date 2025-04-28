from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('moisture/', views.moisture, name='moisture'),
    path('ash/', views.ash, name='ash'),
    path('fat/', views.fat, name='fat'),
    path('fiber/', views.fiber, name='fiber'),
    path('protein/', views.protein, name='protein'),
]
