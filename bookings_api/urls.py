from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.handle_booking),
    path('booking/<int:id>/', views.handle_ticket),
]