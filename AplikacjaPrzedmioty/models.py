from django.db import models


class Przedmiot(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(blank=True, max_length=500)
    cena = models.DecimalField(max_digits=9, decimal_places=2)
