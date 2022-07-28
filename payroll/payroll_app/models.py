from django.db import models

# Create your models here.

# users
class users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    account_type = models.CharField(max_length=20)

# businesses
class businesses(models.Model):
    street_1 = models.CharField(max_length=50)
    street2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    parish = models.CharField()
    country = models.CharField()
    tax_registration_number = models.CharField()
    national_insurnce_scheme = models.CharField()
    business_start_date = models.DateField()

# pay_frequency
class pay_frequency(models.Model):
    business_id = models.IntegerField()
    pay_frequency = models.CharField()
    number_of_periods = models.IntegerField()
    status = models.CharField()

# pay_period
class pay_period(models.Model):
    business_id = models.IntegerField()
    pay_frequency_id = models.IntegerField()
    pay_frequency = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()
    period_number = models.IntegerField()

# company banking details
class company_banking_details(models.Model):
    business_id = models.IntegerField()
    account_name = models.CharField()
    bank_name = models.CharField()
    branch = models.CharField()
    account_number = models.IntegerField(max_length=30)
    account_type = models.CharField()

# employee 
class employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class earnings_type(models.Model):
    earning_type = models.CharField(max_length=50)
