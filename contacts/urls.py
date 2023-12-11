from django.urls import path
from .views import ContactListCreateView, ContactDetailView
from contacts import views


urlpatterns = [
    path('contacts/', views.ContactListCreateView.as_view()),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view()),
]