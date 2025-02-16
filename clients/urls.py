from django.urls import path
from .views import (
    ClientListView,
    ClientDetailView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
)

urlpatterns = [
    path('', ClientListView.as_view(), name='client-list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client/add/', ClientCreateView.as_view(), name='client-add'),
    path('client/<int:pk>/edit/', ClientUpdateView.as_view(), name='client-edit'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
]
