from django.db import models
from django.utils import timezone


class product(models.Model):
    pid = models.IntegerField(primary_key=True)
    pcat = models.CharField(max_length=20)
    pname = models.CharField(max_length=20)
    pdscnt = models.DecimalField(max_digits=10, decimal_places=4)
    pcost = models.DecimalField(max_digits=10, decimal_places=4)
    pmfdt = models.DateField()
    pexpdt = models.DateField()
    pimage=models.ImageField(upload_to='media', blank=True)
    def __str__(self):
        return str(self.pid)


class stock(models.Model):
    prodid = models.OneToOneField(
        product,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    totqty = models.IntegerField()
    last_update = models.DateField()
    next_update = models.DateField()

# Create your models here.
