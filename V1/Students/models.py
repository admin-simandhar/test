from django.db import models
from FunctionManger.DateTimeManager import get_date_time_db
# Create your models here.
class Students(models.Model):
    name            =       models.CharField(max_length=32)
    profile_img     =       models.CharField(max_length=128)
    created         =       models.DateTimeField(default=get_date_time_db())
    class Meta:
        db_table = "students"

class StudentsCourse(models.Model):
    std             =       models.ForeignKey(Students,on_delete=models.CASCADE)
    course          =       models.CharField(max_length=32)
    class Meta:
        db_table = "Students_course"


class StudentsPlacement(models.Model):
    std          =       models.ForeignKey(Students,on_delete=models.CASCADE)
    company         =       models.CharField(max_length=64)
    placement_date  =       models.DateField()

class StudentsScore(models.Model):
    std_id          =       models.ForeignKey(Students,on_delete=models.CASCADE)
    bec             =       models.CharField(max_length=32)
    reg             =       models.CharField(max_length=32)
    far             =       models.CharField(max_length=32)
    aud             =       models.CharField(max_length=32)


