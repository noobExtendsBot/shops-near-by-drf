from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField

from geoapp.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    location = PointField()

    class Meta:
        model = Shop
        fields = '__all__'
