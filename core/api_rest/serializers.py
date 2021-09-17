from rest_framework import serializers
from core.models import *

class HospedeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Hospede
        fields = ('nome','adultos','celular')


class ImovelSerializers(serializers.ModelSerializer):
    hospede=HospedeSerializers
    class Meta:
        model= Imovel
        fields= ('codigo_imovel','telefone','endereço')

class BookingSerializers(serializers.ModelSerializer):
    hospede=HospedeSerializers
    imovel=ImovelSerializers
    class Meta:
        model= Booking
        fields =('checkin_date','checkout_date','check_out','valor','diarias','charge','limpeza')