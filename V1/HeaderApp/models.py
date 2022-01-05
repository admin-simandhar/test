from django.db import models

# Create your models here.

class HeaderBanner(models.Model):
    
    alttag            =     models.CharField(max_length=128)
    media_url         =     models.CharField(max_length=128)
    priority          =     models.IntegerField()
    created           =     models.DateTimeField()
    updated           =     models.DateTimeField()
    
    class Meta:
        db_table = 'header_banner'