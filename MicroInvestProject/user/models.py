from django.db import models
# Create your models here.

class User(models.Model):
    name = models.TextField()
    nid = models.IntegerField(unique=True)
    dob = models.DateField(null=True)
    cell = models.IntegerField(max_length=11)
    email = models.EmailField()
    password = models.TextField()
    isActive = models.BooleanField(default=False)
    isInvestor = models.BooleanField(default=False)
    isEntrepreneur = models.BooleanField(default=False)
    isAnalyst = models.BooleanField(default=False)
    totalInvested = models.FloatField(default=0.00)
    totalWithdrawn = models.FloatField(default=0.00)
