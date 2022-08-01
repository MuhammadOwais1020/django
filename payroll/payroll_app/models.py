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
    business_name = models.CharField(max_length=50)
    street_1 = models.CharField(max_length=50)
    street2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    parish = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    tax_registration_number = models.CharField(max_length=50)
    national_insurnce_scheme = models.CharField(max_length=50)
    business_start_date = models.DateField()
    user_id = models.IntegerField()

# pay_frequency
class pay_frequency(models.Model):
    pay_frequency = models.CharField(max_length=50)
    number_of_periods = models.IntegerField()
    status = models.CharField(max_length=50)

# pay_period
class pay_period(models.Model):
    pay_frequency = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    period_number = models.IntegerField()

# payroll
class payroll(models.Model):
    business_id = models.IntegerField()
    pay_period_id = models.IntegerField()
    status = models.CharField(max_length=30)


# company banking details
class company_banking_details(models.Model):
    business_id = models.IntegerField()
    account_name = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account_number = models.BigIntegerField()
    account_type = models.CharField(max_length=50)

# employee 
class employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    start_date = models.DateField()
    work_address = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    TRN = models.IntegerField()
    NIS = models.IntegerField()
    contact_number = models.BigIntegerField()
    personal_email_address = models.EmailField()
    next_of_kin = models.CharField(max_length=50)
    contact_number_of_next_of_kin = models.BigIntegerField()
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50)
    city_town = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    parish = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    user_id = models.IntegerField()
    business_id = models.IntegerField()

# earning type
class earnings_type(models.Model):
    earning_type = models.CharField(max_length=50)

# earnings
class earnings(models.Model):
    employee_id = models.IntegerField()
    earning_type = models.CharField(max_length=50)
    PTD_amount = models.IntegerField()
    taxable = models.CharField(max_length=50)
    pay_frequency = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)

# deduction
class deduction(models.Model):
    employee_id = models.IntegerField()
    deduction_type = models.CharField(max_length=50)
    amount = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)

# paymentTerm
class paymentTerm(models.Model):
    employee_id = models.IntegerField()
    payment_term = models.CharField(max_length=50)

# employee banking details
class employee_banking_details(models.Model):
    employee_id = models.IntegerField()
    bank_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=50)