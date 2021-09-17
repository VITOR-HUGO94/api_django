from django.db import models
from datetime import datetime,date,timedelta
from django.dispatch import receiver
from django.db.models.signals import post_save
from uuid import uuid4

class Hospede(models.Model):
    nome = models.CharField(max_length=200)
    adultos=models.IntegerField(default=0)
    celular=models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Imovel(models.Model):
    #hospede = models.ForeignKey(Hospede,on_delete=models.CASCADE)
    codigo_imovel = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    telefone=models.CharField(max_length=13)
    endereço= models.CharField(max_length=200)
    

    def __str__(self):
        return self.codigo_imovel



class Booking(models.Model):
    #hospede = models.ForeignKey(Hospede ,on_delete=models.CASCADE)
    #imovel = models.ForeignKey(Imovel ,on_delete=models.CASCADE)
    checkin_date = models.DateTimeField(default=datetime.now())
    checkout_date = models.DateTimeField(default=datetime.now() + timedelta())
    check_out = models.BooleanField(default=False)
    valor = models.IntegerField(default=0)
    
    

    def charge(self):
        
        if self.check_out:
            if self.checkin_date==self.checkout_date:

                return self.valor
            else:
                time_delta = self.checkout_date - self.checkin_date
                total_time = time_delta /86400
                total_cost = total_time * self.valor
                # return total_cost
                return total_cost
        else:
            return 'calculated when checked out'
    
    def diarias(self):
        if self.check_out:
            time_delta = self.checkout_date - self.checkin_date
            total_time = time_delta /86400
            diarias = total_time * 1
            return diarias
    
    def limpeza(self):
        if self.check_out:
            datahora = self.checkout_date

            return datahora

   

