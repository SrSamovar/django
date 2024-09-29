# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializers, MeasurementSerializers


class SensorCreateView(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers


class SensorUpdateView(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers


class MeasurementCreateView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializers


class ListSensorView(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = [{'id': sensor['id'], 'name': sensor['name'], 'description': sensor['description']}
                for sensor in serializer.data]
        return Response(data)
