from django.contrib import admin
from .models import Investment
# Register your models here.

#class InvestmentModelAdmin(admin.ModelAdmin):
#    list_display = (
#        'investment_ID',
#        'investor_ID',
#        'project_ID',
#        'amount'
#    )
admin.site.register(Investment)
