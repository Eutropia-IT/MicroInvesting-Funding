from django.db import models
from datetime import datetime
# Create your models here.

class ResetPssDB(models.Model):
    applyUserEmail = models.EmailField()
    secritKey = models.TextField(default='')
    date = models.DateTimeField(default=datetime.now)
