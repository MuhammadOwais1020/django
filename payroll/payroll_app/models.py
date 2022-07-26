from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    account_type = models.CharField(max_length=20)

class earnings_type(models.Model):
    earning_type = models.CharField(max_length=50)
