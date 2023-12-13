from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoiceNumber = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    sender = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    dueDate = models.CharField(max_length=255)