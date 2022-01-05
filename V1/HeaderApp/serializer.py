from rest_framework import serializers
from HeaderApp.models import HeaderBanner
class HeaderBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model       =   HeaderBanner
        fields = "__all__"