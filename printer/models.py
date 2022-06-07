from django.db import models


class Region(models.Model):
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Address(models.Model):
    address = models.CharField("Адрес", max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"


class Printer(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    ip_address = models.CharField("IP адрес", max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Принтер"
        verbose_name_plural = "Принтеры"
