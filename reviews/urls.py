from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='reviews_index'),
    path('about/', views.about, name='reviews_about'),
]
