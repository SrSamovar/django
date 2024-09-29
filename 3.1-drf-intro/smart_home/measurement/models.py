from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.IntegerField(verbose_name='температура')
    created_at = models.DateField(verbose_name='время измерения', auto_now_add=True)

    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sensor.name} - {self.temperature}'
