import email
from xml.dom.minidom import NamedNodeMap
from django.http import HttpResponse
from django.shortcuts import render
from payroll_app.models import pay_frequency
from payroll_app.models import users
from payroll_app.models import earnings_type
from payroll_app.models import pay_period
from payroll_app.models import businesses

# Create your views here.

# admin
def admin(request):
    login = "success"
    data = {
        "login" : login
    }
    return render(request, "admin.html", data)


def admin_f(request):
    return render(request, "admin.html")

# index
def home(request):
    data = {
        "login":"",
        "account_type":""
    }
    return render(request, "index.html", data)

# admin login
def adminLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

    login = ""
    
    if username == 'admin' and password == "123":
        login = "success"
    else:
        login = "error"
    
    data = {
        "login" : login
    }

    return render(request, "admin.html", data)

# create user
def createUser(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile-number')
        password = request.POST.get('password')
        account_type = request.POST.get('account-type')
    
        en = users(first_name=first_name,last_name=last_name,email=email,mobile_number=mobile_number,password=password,account_type=account_type)
    
        print(en)
        save = ""
    
        try:
            en.save()
            save = "success"
        except:
            save = "error"

    data = {
        "save": save,
        "login":"er"
    }
    
    return render(request, "admin.html", data)

def allUsers(request):
    data={}
    fetchData = users.objects.all()
    print(fetchData)
    data = {
        "users": fetchData
    }
    return render(request, "all-users.html", data)

def userLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
    
    print(username)

    record = users.objects.filter(email=email,password=password)
    # access earning types from database
    earnings_type_lst = earnings_type.objects.all()

    first_name = ""
    last_name = ""
    email = ""
    mobile_number = ""
    account_type = ""
    login = ""
    id = 0
    is_business = ""
    business = "n"

    for a in record:
        id = a.id
        first_name = a.first_name
        last_name = a.last_name
        email = a.email
        mobile_number = a.mobile_number
        account_type = a.account_type

    if first_name == "":
        login = 'error'
    else:
        login = "success"

        is_business = businesses.objects.filter(user_id = id)
        for b in is_business:
            business = b.id

        if business != "":
            business = "y"
    
    pay_period_record_monthly = ""
    pay_period_record_fortnightly = ""
    pay_period_record_bi_weekly = ""
    pay_period_record_weekly = ""
    pay_period_record_hourly = ""

    pay_period_record_monthly = pay_period.objects.filter(pay_frequency = "Monthly")
    pay_period_record_fortnightly = pay_period.objects.filter(pay_frequency = "Fortnightly")
    pay_period_record_bi_weekly = pay_period.objects.filter(pay_frequency = "Bi-Weekly")
    pay_period_record_weekly = pay_period.objects.filter(pay_frequency = "Weekly")
    pay_period_record_hourly = pay_period.objects.filter(pay_frequency = "Hourly")


    data={
        "login" : login,
        "first_name" : first_name,
        "last_name": last_name,
        "email":email,
        "mobile_number":mobile_number,
        "account_type":account_type,
        "earning_type":earnings_type_lst,
        "b_id": business,
        "pay_period_record_monthly":  pay_period_record_monthly,
        "pay_period_record_fortnightly":  pay_period_record_fortnightly,
        "pay_period_record_bi_weekly":  pay_period_record_bi_weekly,
        "pay_period_record_weekly":  pay_period_record_weekly,
        "pay_period_record_hourly":  pay_period_record_hourly
    }

    return render(request, "index.html", data)

# Logout Account
def logout(request):
    return render(request, "index.html")

# admin Logout
def adminLogout(request):
    return render(request, "admin.html")

# create business
def createBusiness(request):
    if request.method == "POST":
        # dashboard information
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile-number')
        account_type = request.POST.get('account-type')
        # business information

    data = {
        "login": "success",
        "account_type": "Business",
        "email": email,
        "first_name": first_name,
        "last_name":last_name,
        "mobile_number": mobile_number,
        "account_type": account_type
    }
    return render(request, 'index.html', data)

# pay period 
def payPeriod(request):
    return render(request, "pay-period.html")

# create Pay Period
def createPayPeriod(request):
    save = ""
    if request.method == "POST":
        pay_frequency = request.POST.get('frequency')
        start_date = request.POST.get('start-date')
        end_date = request.POST.get('end-date')
        period_number = request.POST.get('period-number')

        # record save into database
        en = pay_period(pay_frequency = pay_frequency, start_date = start_date, end_date = end_date, period_number = period_number)

    
        try:
            en.save()
            save = "success"
        except:
            save = "error"

    pay_period_record = pay_period.objects.all()

    data = {
        "save": save,
        "pay_period_record": pay_period_record
    }

    return render(request, "pay-period.html", data)