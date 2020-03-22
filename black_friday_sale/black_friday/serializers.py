from rest_framework import serializers
from black_friday.models import price
class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = price
        fields = '__all__'