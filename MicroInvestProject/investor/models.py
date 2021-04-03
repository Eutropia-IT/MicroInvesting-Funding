from entrepreneur.models import Projects
from user.models import User
from django.db import models
from datetime import datetime
# Create your models here.

class Investment(models.Model):
    investor_ID = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    proj_ID = models.ForeignKey(Projects, on_delete=models.DO_NOTHING)
    amount = models.FloatField(default=0.0)
    investmentDate = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return '%s' % (self.investor_ID)