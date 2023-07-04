from django.db import models

# Create your models here.
Choice_Of_Day = {
    'mr': 'Morning',
    'af': 'Afternoon',
    'ng': 'Night'
}

class Account(models.Model):
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    accountBalance = models.FloatField()
    password = models.CharField

    
    