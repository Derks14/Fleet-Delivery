from django.db import models

# Create your models here.

from dashboard.models import Transit


class User(models.Model):
    firstname = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=13, null=True)
    username = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    postal = models.CharField(max_length=100, null=True)
    about = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.firstname


class Item(models.Model):

    item_description = models.TextField(help_text='A brief descripton of item. eg. electronics, letter, etc')
    tracking_number = models.CharField(max_length=12, help_text='A 12 digit Unique number')
    serial_pin = models.CharField(max_length=6, help_text='A unique pin in the form of password')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=100, help_text='Please state fleet service type item is registered for', null=True)
    weight = models.CharField(max_length=10, help_text='Please enter the weight of item', null=True)
    transit = models.ManyToManyField(Transit, help_text='Add a transit for this item')

    def __str__(self):
        return self.tracking_number


class Comment(models.Model):
    enquiry = models.TextField(max_length=1000, help_text='Includes comments', null=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    emailaddress = models.CharField(max_length=100)
    telephone = models.CharField(max_length=13)

    def __str__(self):
        return self.enquiry
