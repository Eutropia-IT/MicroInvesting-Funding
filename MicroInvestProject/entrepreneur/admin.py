from django.contrib import admin
from .models import Projects
# Register your models here.


#class ProjectsModelAdmin(admin.ModelAdmin):
    #list_display = (
     #   "entr_ID", 
      #  "proj_Name", 
       # "proj_Location", 
        #"proj_Budget ",
        #"proj_Funded",
        #"profit_Indicator1", 
        #"profit_Indicator2", 
        #"profit_Indicator3", 
        #"feedback1", 
        #"feedback2",
        #"feedback3"        
    #)
admin.site.register(Projects)