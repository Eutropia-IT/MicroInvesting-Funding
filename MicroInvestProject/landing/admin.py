from django.contrib import admin
from .models import ResetPssDB 

# Register your models here.
class ResetPssDBModelAdmin(admin.ModelAdmin):
    list_display = (
        'applyUserEmail',
    )
admin.site.register(ResetPssDB,ResetPssDBModelAdmin)