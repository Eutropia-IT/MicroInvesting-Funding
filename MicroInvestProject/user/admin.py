from django.contrib import admin
from .models import User, Transaction
# Register your models here.


class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'nid',
        'dob',
        'cell',
        'email',
        'password',
        'isActive',
        'isInvestor',
        'isEntrepreneur',
        'isAnalyst',
        'totalInvested',
        'totalWithdrawn',
        'joiningDate',
    )
admin.site.register(User,UserModelAdmin)


class TransactionModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'trans_type',
        'user_ID',
        'amount',
        'transactionDate',
    )

admin.site.register(Transaction,TransactionModelAdmin)
