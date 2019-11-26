from django.db import models

# # Create your models here.
class cart(models.Model):
    username = models.EmailField(max_length=20)
    pid = models.IntegerField()
    units = models.IntegerField()
    unitprice = models.DecimalField(max_digits=10,decimal_places=4)
    tuprice = models.DecimalField(max_digits=10,decimal_places=4)
    image=models.ImageField(blank=True)

