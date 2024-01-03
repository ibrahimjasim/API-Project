from django.urls import path
from .views import EventListCreateView, EventDetailView, EventDeleteView, EventUpdateView
from events import views


urlpatterns = [
    path('events/', views.EventListCreateView.as_view()),
    path('events/<int:pk>/', views.EventDetailView.as_view()),
    path('event/edit/<int:pk>/', EventUpdateView.as_view(), name='event-edit'),
    path('event/delete/<int:pk>/', EventDeleteView.as_view(), name='event-delete'),
]