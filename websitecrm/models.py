from django.db import models

# Create your models here.
class record(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    first_name =  models.CharField( max_length=50)
    last_name =  models.CharField( max_length=50)
    phone =    models.CharField( max_length=50)
    email =    models.CharField( max_length=50)
    city =    models.CharField( max_length=50)
    state  =   models.CharField( max_length=50, blank=True, null=True)
    zipCode  =   models.CharField( max_length=20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name} {self.phone}")
    
