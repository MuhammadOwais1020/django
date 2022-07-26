import email
from django.shortcuts import render
from payroll_app.models import users
from payroll_app.models import earnings_type

# Create your views here.

# admin
def admin(request):
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

    record = users.objects.filter(email=email,password=password)
    # access earning types from database
    earnings_type_lst = earnings_type.objects.all()

    first_name = ""
    last_name = ""
    email = ""
    mobile_number = ""
    account_type = ""
    login = ""

    for a in record:
        first_name = a.first_name
        last_name = a.last_name
        email = a.email
        mobile_number = a.mobile_number
        account_type = a.account_type

    if first_name == "":
        login = 'error'
    else:
        login = "success"

    data={
        "login" : login,
        "first_name" : first_name,
        "last_name": last_name,
        "email":email,
        "mobile_number":mobile_number,
        "account_type":account_type,
        "earning_type":earnings_type_lst
    }

    return render(request, "index.html", data)

# Logout Account
def logout(request):
    return render(request, "index.html")