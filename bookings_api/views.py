from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import time
from bookings_api.models import Booking
from bookings_api.serializers import AllBookingsSerializer
from bookings_api.serializers import TicketTimingSerializer
from bookings_api.serializers import UserDetailSerializer
from bookings_api.serializers import InsertNewTicket


@api_view(['GET','POST'])
def handle_booking(request):
    if request.method == 'GET':
        tickets = Booking.objects.all()
        date = request.GET.get('date', '')
        ptime = request.GET.get('time', '')
        if date is not '' and ptime is not '':
            tickets = tickets.filter(date = date, time = ptime)
            serializer = TicketTimingSerializer(tickets, many = True)
            return Response(serializer.data)
        serializer = AllBookingsSerializer(tickets, many = True)
        return Response(serializer.data)


    elif request.method == 'POST':
        schedule = [time(8,0,0), time(10,45,0), time(13,30,0), time(16,15,0), time(19,0,0), time(21,45,0)]
        ptime = request.data.get('time', '')
        if ptime is not '':
            print(ptime)
            try:
                ptime = ptime.split(':')
                req_time = time(int(ptime[0]), int(ptime[1]))
            except:
                return Response({"status": "Failure", "Description" : "Invalid time format"})

            if req_time not in schedule:
                return Response({"status": "Failure", "Description" : "Time provided is not scheduled"})

            try:
                entry_count = Booking.objects.all().filter(time=req_time, date=request.data.get('date', '')).count()
            except:
                return Response({"status": "Failure", "Description" : "Invalid date format"})
            if entry_count >= 20:
                return Response({"status": "Failure", "Description" : "Time slot is completely booked"})


        data = request.data
        serializer = InsertNewTicket(data = data)
        if serializer.is_valid():
            ticket_instance = Booking.objects.create(**serializer.data)
            return Response({"Status":"Success", "Description": "Ticket {} sucessfully created".format(ticket_instance.ticket_id)})
        else:
            return Response({"errors": serializer.errors})




@api_view(['GET', 'PATCH', 'DELETE'])
def handle_ticket(request, id):
    if request.method == 'GET':
        try:
            ticket = Booking.objects.get(ticket_id = id)
        except Booking.DoesNotExist:
            return Response({"status": "Failure", "Description" : "Not found"})
        serializer = UserDetailSerializer(ticket)
        return Response(serializer.data)


    elif request.method == 'PATCH':
        try:
            ticket = Booking.objects.get(ticket_id = id)
        except Booking.DoesNotExist:
            return Response({"status": "Failure", "Description" : "Not found"})
        schedule = [time(8,0,0), time(10,45,0), time(13,30,0), time(16,15,0), time(19,0,0), time(21,45,0)]
        date = request.data.get('date', '')
        ptime = request.data.get('time', '')
        if date is not '' and time is not '':
            try:
                ptime = ptime.split(':')
                req_time = time(int(ptime[0]), int(ptime[1]))
            except:
                return Response({"status": "Failure", "Description" : "Invalid time format"})

            if req_time not in schedule:
                return Response({"status": "Failure", "Description" : "Time provided is not scheduled"})

            try:
                entry_count = Booking.objects.all().filter(time=req_time, date=request.data.get('date', '')).count()
            except:
                return Response({"status": "Failure", "Description" : "Invalid date format"})
            if entry_count >= 20:
                return Response({"status": "Failure", "Description" : "Time slot is completely booked"})

            try:
                ticket.date = date
                ticket.time = req_time
                ticket.save()
                return Response({"status" : "Success", "Description": "Ticket updated successfully"})
            except:
                return Response({"status": "Failure", "Description" : "Invalid data format"})
        
        return Response({"status": "Failure", "Description" : "Incomplete data"})


    elif request.method == 'DELETE':
        try:
            ticket = Booking.objects.get(ticket_id = id)
        except Booking.DoesNotExist:
            return Response({"status": "Failure", "Description" : "Not found"})

        ticket.delete()
        return Response({"status" : "Success", "Description": "Ticket deleted successfully"})

