from django.db import models

# Create your models here.
class Printer(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    ip_address = models.CharField("IP адрес", max_length=255)
    adress = models.ForeignKey("Address")


class Address(models.Model):
    address = models.CharField("Адрес", max_length=255)
    region = models.ForeignKey()


class Region(models.Model):
    name = models.CharField("Название", max_length=255)


class Branch(models.Model):
    name = models.CharField("Название", max_length=255)

