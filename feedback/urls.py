from django.urls import path
from . import views


urlpatterns = [
    path('feedback/', views.add_feedback, name='feedback'),
    path('review/', views.add_review, name='review'),
    path('feedback_create', views.feedback_create, name='create_feedback')
]