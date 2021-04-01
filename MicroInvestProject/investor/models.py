from entrepreneur.models import Projects
from user.models import User
from django.db import models

# Create your models here.

class Investment(models.Model):
    investor_ID = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    proj_ID = models.ForeignKey(Projects, on_delete=models.DO_NOTHING)
    amount = models.FloatField(default=0.0)
    