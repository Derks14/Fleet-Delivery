from django.db import models
# Create your models here.


class Transit(models.Model):

    class Route(models.IntegerChoices):
        AIR = 1
        SEA = 2
        LAND = 3
    route = models.IntegerField(choices=Route.choices, help_text='How is item been transported', null=True)

    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    pickup = models.CharField(max_length=100, null=True, blank=True, help_text='Item was picked up from')
    destination = models.CharField(max_length=100, null=True, blank=True, help_text='Where item is been delivered')
    region = models.CharField(max_length=100, help_text='Current Country or region of item')
    activity = models.TextField(help_text='Whats happening to item at current region')

    def __str__(self):
        return self.activity


# Transit.objects.get(item__tracking_number='348839043453')