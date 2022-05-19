from django.urls import path
from . import views

urlpatterns = [
    path('rating', views.ratingsView.as_view(), name='rating'),
    path('failed', views.failed, name='failed'),
    path('dyn_rating', views.dyn_ratings, name='dyn_rating'),
]
