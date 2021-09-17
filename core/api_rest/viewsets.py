from django.shortcuts import render
from rest_framework import viewsets
from core.api_rest import serializers
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework import generics
# from django.shortcuts import get_list_or_404
# from rest_framework.generics import ListAPIView
from core.models import *

from core import *
class HospedeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HospedeSerializers
    queryset = models.Hospede.objects.all()
    
    @api_view(['GET','POST'])
    def api_hospede_list_view(request):
        hospede=Hospede.objects.all()
        if request.method=='GET':
            serializer=HospedeSerializers(hospede,many=True)
            return Response(serializer.data)
        if request.method =='POST':
            serializer=HospedeSerializers(data=request.data)
            if serializer.is_valid():
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)                    

    
class ImovelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelSerializers
    queryset = models.Imovel.objects.all()   
    
    @api_view(['GET','POST'])
    def api_imovel_list_view(request):
        imovel=Imovel.objects.all()
        if request.method =='GET':
            serializer=ImovelSerializers(imovel,many=True)
            return Response(serializer.data)
        if request.method=='POST':
            # data={}
            serializer=ImovelSerializers(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                # return 'created Successfully'
                return Response(data,status=status.HTTP_201_CREATED)   
            else:
                # return 'Creation not succesfull'
                return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookingSerializers
    queryset = models.Booking.objects.all()

    @api_view(['GET','POST'])
    def api_booking_list_view(request):
        booking=Booking.objects.all()
        if request.method =='GET':
            serializer=BookingSerializers(booking,many=True)
            return Response(serializer.data)
        if request.methos=='POST':
            serializer=BookingSerializers(data=request.data)
            if serializer.is_valid():
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)        