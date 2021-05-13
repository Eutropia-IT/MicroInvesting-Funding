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
    currentBalance = models.FloatField(default=0.00)
    totalInvested = models.FloatField(default=0.00)
    totalRepaid = models.FloatField(default=0.00)
    profileImage = models.FileField(upload_to='profile', default="default.jpg")
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
    amount = models.FloatField(default=0.0)
    transactionDate = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return '%s' % (self.user_ID)

