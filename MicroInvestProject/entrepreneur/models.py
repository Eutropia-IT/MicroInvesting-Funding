from user.models import User
from django.db import models

# Create your models here.

class Projects(models.Model):
    entr_ID = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    proj_Name = models.TextField()
    proj_Location = models.TextField()
    proj_Budget = models.FloatField(default=0.0)
    proj_Funded = models.FloatField()
    profit_Indicator1 = models.FloatField(default=0.00)
    profit_Indicator2 = models.FloatField(default=0.00)
    profit_Indicator3 = models.FloatField(default=0.00)
    feedback1 = models.TextField()
    feedback2 = models.TextField()
    feedback3 = models.TextField()
    