from django.db import models

# Create your models for Vendor and bidder here.
class VendorMdel(models.Model):
    first_name       = models.CharField(max_length=30)
    last_name        = models.CharField(max_length=30)
    email            = models.EmailField(max_length=40)
    conform_email    = models.EmailField(max_length=40)
    password         = models.CharField(max_length=30)
    conform_password = models.CharField(max_length=30)
    company_name     = models.CharField(max_length=25)
    mobile_number    = models.IntegerField()
    telephone_number = models.IntegerField()
    address1         = models.TextField(max_length=50)
    address2         = models.TextField(max_length=50)
    city             = models.CharField(max_length=30)
    postal_code      = models.IntegerField()
    select_country = (
        ('USA','USA'),
        ('India','India'),
        ('UK','UK'),
        ('Canada','Canada')
    )
    country          = models.CharField(max_length=15, choices= select_country)
    state            = models.CharField(max_length=15)





