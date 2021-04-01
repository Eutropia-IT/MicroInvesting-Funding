from django.contrib import admin
from .models import User, Transaction
# Register your models here.


# class UserModelAdmin(admin.ModelAdmin):
#     list_display = (
#         'user_id',
#         'name',
#         'nid',
#         'dob',
#         'cell',
#         'email',
#         'password',
#         'isActive',
#         'isInvestor',
#         'isEntrepreneur',
#         'isAnalyst',
#         'totalInvested',
#         'totalWithdrawn'
#     )
admin.site.register(User)


# class TransactionModelAdmin(admin.ModelAdmin):
#     list_display = (
#         'transaction_id',
#         'transaction_type',
#         'user_id',
#         'amount'
#     )

admin.site.register(Transaction)
