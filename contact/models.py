from django.db import models

# Create your models here

class Info(models.Model):
    place = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField( max_length=30 )

    class Meta :
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")


    def __str__(self):
        return self.email

    
