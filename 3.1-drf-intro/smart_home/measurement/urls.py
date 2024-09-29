from django.urls import path
from .views import SensorCreateView, SensorUpdateView, MeasurementCreateView, ListSensorView, SearchSensorView

urlpatterns = [
    path('sensors/', ListSensorView.as_view(), name='sensor_list'),
    path('sensors/create/', SensorCreateView.as_view(), name='sensor_create'),
    path('sensors/update/<int:pk>/', SensorUpdateView.as_view(), name='sensor_update'),
    path('measurements/create/', MeasurementCreateView.as_view(), name='measurement_create'),
    path('sensor/<int:pk>', SearchSensorView.as_view(), name='sensor_search')
]
