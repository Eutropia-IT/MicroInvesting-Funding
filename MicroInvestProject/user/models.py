from django.db import models
from django.db.models.deletion import DO_NOTHING
from datetime import datetime
# Create your models here.

class User(models.Model):
    name = models.TextField()
    nid = models.IntegerField(unique=True)
    dob = models.DateField(null=True)
    cell = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.TextField()
    isActive = models.BooleanField(default=False)
    isInvestor = models.BooleanField(default=False)
    isEntrepreneur = models.BooleanField(default=False)
    isAnalyst = models.BooleanField(default=False)
    totalInvested = models.FloatField(default=0.00)
    totalWithdrawn = models.FloatField(default=0.00)
    joiningDate = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return '%s' % (self.id)

class Transaction(models.Model):
    Deposit = 'deposit'
    Withdraw = 'withdraw'
    options = [
        (Deposit, 'deposit'),
        (Withdraw, 'withdraw'),
    ]
    trans_type = models.TextField(choices=options)
    user_ID = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    transactionDate = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return '%s' % (self.user_ID)

