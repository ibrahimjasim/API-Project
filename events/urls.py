from django.urls import path
from .views import EventListCreateView, EventDetailView
from events import views


urlpatterns = [
    path('events/', views.EventListCreateView.as_view()),
    path('events/<int:pk>/', views.EventDetailView.as_view()),
]