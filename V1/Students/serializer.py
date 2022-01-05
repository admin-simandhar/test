from rest_framework import serializers
from Students.models import Students,StudentsCourse
from rest_framework.exceptions import ValidationError

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model               =       Students
        fields              =       "__all__"

class StudentsCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model               =       StudentsCourse
        fields              =       "__all__"

    def validate(self, attrs):
        accept_only_courses =   ["cpa","cma","ea","ifrs"]
        if not attrs["course"] in accept_only_courses:
            raise ValidationError({"unnknown course": attrs["course"]})
        
        return super().validate(attrs)