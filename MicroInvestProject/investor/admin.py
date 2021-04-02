from django.contrib import admin
from .models import Investment
# Register your models here.

class InvestmentModelAdmin(admin.ModelAdmin):
   list_display = (
       'id',
       'investor_ID',
       'proj_ID',
       'amount',
       'investmentDate',
   )
admin.site.register(Investment,InvestmentModelAdmin)
