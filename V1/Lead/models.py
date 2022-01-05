from django.db import models

class Leads(models.Model):
    firstname       =       models.CharField(max_length=32)
    lastname        =       models.CharField(max_length=32)
    email           =       models.CharField(max_length=64,unique=True)
    phone           =       models.CharField(max_length=16, unique=True)
    select_course   =       models.CharField(max_length=32)
    qualification   =       models.CharField(max_length=32)
    city            =       models.CharField(max_length=32)
    source          =       models.CharField(max_length=32)
    medium          =       models.CharField(max_length=32)
    campaign        =       models.CharField(max_length=32)
    created         =       models.DateTimeField()
    ls_record       =       models.BooleanField(default=False)
    
    class Meta:
        db_table = "leads"

        