from django.db import models

# Create your models here.
class User(models.Model):
    username            = 	models.CharField(max_length=64,unique=True)
    password            =   models.CharField(max_length=64)
    fullname            =   models.CharField(max_length=32)
    is_super_admin      =   models.BooleanField(default=False)
    
#    department          =  models.ManyToManyField(Department)
    
    # def __str__(self):
    #     return self.fullname
    
    class Meta:
        db_table = 'user'