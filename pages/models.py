from django.db import models

class House(models.Model):
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    rooms = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.address