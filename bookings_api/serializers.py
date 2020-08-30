from rest_framework import serializers
from .models import Booking

class AllBookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['ticket_id', 'user_name', 'phone_number', 'date', 'time', 'status']

class TicketTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['ticket_id']

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user_name', 'phone_number']

class InsertNewTicket(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user_name', 'phone_number', 'date', 'time', 'status']
