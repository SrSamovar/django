from rest_framework import serializers
from .models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы


class MeasurementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at', 'sensor']


class SensorSerializers(serializers.ModelSerializer):
    measurements = MeasurementSerializers(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
