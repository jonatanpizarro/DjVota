from django.db import models
from django.conf import settings




class Consulta(models.Model):
    consulta_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date end')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    def __str__(self):
        return self.consulta_text


class Opcion(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    opcion_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.opcion_text


class Voto(models.Model):
	opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    
    

class Invitacion(models.Model):
	consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
	email = models.CharField(max_length=200)