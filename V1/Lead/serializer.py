from django.db import models
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Leads
from django.core.validators import validate_email


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = "__all__"
    

    def validate(self, attrs):
        required        =   ["firstname","lastname","email","phone"]
        input_attrbs    =   attrs.keys()
        res             =   set(required)-set(input_attrbs)

        if len(res):
            raise ValidationError({"fields required": res})
        
        if "email" in input_attrbs:
            validate_email(attrs["email"])
        
        if "phone" in input_attrbs:
            if not attrs["phone"].isdigit():
                raise ValidationError({"phone": ["invalid phone number"]})
            if len(attrs["phone"])<10:
                raise ValidationError({"phone": ["ensure phone number must be greater than 10 digits"]})

        return super().validate(attrs)
