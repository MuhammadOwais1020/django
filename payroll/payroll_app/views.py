import email
from xml.dom.minidom import NamedNodeMap
from django.http import HttpResponse
from django.shortcuts import render
from payroll_app.models import payroll
from payroll_app.models import pay_frequency
from payroll_app.models import users
from payroll_app.models import earnings_type
from payroll_app.models import pay_period
from payroll_app.models import businesses
from payroll_app.models import company_banking_details
from payroll_app.models import payroll

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

        if business != "n":
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

    # fetch business records
    business_record = getBusinessRecords(id)

    data={
        "login" : login,
        "id":id,
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
        "pay_period_record_hourly":  pay_period_record_hourly,
        "user_record": business_record['user_record'],
        "bank_details_record": business_record['bank_details_record'],
        "business_records": business_record['business_records'],
        "payroll_records": business_record['payroll_records']
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
        business_name = request.POST.get('business-name')
        street_1 = request.POST.get('street1')
        street_2 = request.POST.get('street2')
        city_town = request.POST.get('city-town')
        postal_code = request.POST.get('postal-code')
        parish = request.POST.get('parish')
        country = request.POST.get('country')
        trn = request.POST.get('TRN')
        nis = request.POST.get('NIS')
        business_start_date = request.POST.get('business-start-date')
        user_id = request.POST.get('user-id')
        # pay frequency
        pay_frequency_check_box_monthly = request.POST.get('pay-frequency-check-box-monthly')
        pay_frequency_check_box_fortnightly = request.POST.get('pay-frequency-check-box-fortnightly')
        pay_frequency_check_box_bi_weekly = request.POST.get('pay-frequency-check-box-bi-weekly')
        pay_frequency_check_box_weekly = request.POST.get('pay-frequency-check-box-weekly')
        
        pay_frequency_check_box_lst = []

        if pay_frequency_check_box_monthly != "":
            pay_frequency_check_box_lst.append(pay_frequency_check_box_monthly)

        if pay_frequency_check_box_fortnightly != "":
            pay_frequency_check_box_lst.append(pay_frequency_check_box_fortnightly)

        if pay_frequency_check_box_bi_weekly != "":
            pay_frequency_check_box_lst.append(pay_frequency_check_box_bi_weekly)

        if pay_frequency_check_box_weekly != "":
            pay_frequency_check_box_lst.append(pay_frequency_check_box_weekly)
        
        # pay period data will store in payroll table just pay period id and business id
        pay_period_id_monthtly = request.POST.get('monthly-pay-start-date')
        pay_period_fortnightly = request.POST.get('fortnightly-pay-start-date')
        pay_period_id_bi_weekly = request.POST.get('bi-weekly-pay-start-date')
        pay_period_id_weekly = request.POST.get('weekly-pay-start-date')
        
        pay_period_id_lst = []
        
        if pay_period_id_monthtly != "":
            pay_period_id_lst.append(pay_period_id_monthtly)
        
        if pay_period_fortnightly != "":
            pay_period_id_lst.append(pay_period_fortnightly)

        if pay_period_id_bi_weekly != "":
            pay_period_id_lst.append(pay_period_id_bi_weekly)

        if pay_period_id_weekly != "":
            pay_period_id_lst.append(pay_period_id_weekly)
        
        print(pay_period_id_lst)
        # company banking details
        account_name = request.POST.get('account-name')
        account_number = request.POST.get('account-number')
        bank_name = request.POST.get('bank-name')
        branch_name = request.POST.get('branch-name')
        account_type = request.POST.get('account-type')

        # insert data into business table 
        bd = businesses(business_name=business_name, street_1=street_1, street2=street_2, city=city_town, postal_code=postal_code, parish=parish, country=country, tax_registration_number=trn, national_insurnce_scheme=nis, business_start_date=business_start_date, user_id=user_id)
        bd.save()
        
        # fetch last business id
        business_id = ""
        business_records = businesses.objects.raw('SELECT * FROM payroll_app_businesses ORDER BY id DESC LIMIT 1')
        for a in business_records:
            business_id = a.id

        # insert data into company banking details
        cbd =  company_banking_details(business_id=business_id, account_name=account_name, bank_name=bank_name, branch=branch_name, account_number=account_number, account_type=account_type)
        cbd.save()
        
        # insert data into payroll table
        for payperiodid in pay_period_id_lst:
            # fetch payroll last id
            payroll_id = 1
            payroll_record = payroll.objects.raw('SELECT * FROM payroll_app_payroll ORDER BY id DESC LIMIT 1')
            for a in payroll_record:
                if a.id != "":
                    payroll_id = a.id
            prd = payroll(id=payroll_id, business_id=business_id, pay_period_id=payperiodid, status="Active")
            prd.save()
        
        # insert data into pay_frequency table
        f_p_s = []
        # f_p_s == frequency_period_status
        for payfrequencycheckbox in pay_frequency_check_box_lst:
            f_p_s = payfrequencycheckbox.split(':')
            pf = pay_frequency(pay_frequency=f_p_s[0], number_of_periods=f_p_s[1], status=f_p_s[2])
            pf.save()
    
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

    # fetch business records
    business_record = getBusinessRecords(user_id)

    data = {
        "login": "success",
        "account_type": "Business",
        "email": email,
        "first_name": first_name,
        "last_name":last_name,
        "mobile_number": mobile_number,
        "account_type": account_type,
        "pay_period_record_monthly":  pay_period_record_monthly,
        "pay_period_record_fortnightly":  pay_period_record_fortnightly,
        "pay_period_record_bi_weekly":  pay_period_record_bi_weekly,
        "pay_period_record_weekly":  pay_period_record_weekly,
        "pay_period_record_hourly":  pay_period_record_hourly,
        "b_id":"y",
        "user_record": business_record['user_record'],
        "bank_details_record": business_record['bank_details_record'],
        "business_records": business_record['business_records'],
        "payroll_records": business_record['payroll_records']
    }
    return render(request, 'index.html', data)

# pay period 
def payPeriod(request):
    # fetch all pay period records
    pay_period_record = pay_period.objects.all()

    data = {
        "pay_period_record": pay_period_record
    }
    return render(request, "pay-period.html", data)

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



# business view
def businessView(request):
    if request.method == "POST":
        business_id = request.POST.get('business-id')

        business_record = businesses.objects.filter(id=business_id)
        
        for b in business_record:
            user_id = b.user_id
        
        user_record = users.objects.filter(id=user_id)

        payroll_record = payroll.objects.filter(business_id=business_id)
        pay_period_ids = []
        for id in payroll_record:
            pay_period_ids.append(id.pay_period_id)

        bank_record = company_banking_details.objects.filter(business_id=business_id)

        pay_period_record = []
        for id in pay_period_ids:
            pay_period_record.append(pay_period.objects.filter(id=id))

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

        data = {
            "pay_period_record":pay_period_record,
            "bank_record":bank_record,
            "user_record":user_record,
            "business_record":business_record,
            "pay_period_record_monthly":  pay_period_record_monthly,
            "pay_period_record_fortnightly":  pay_period_record_fortnightly,
            "pay_period_record_bi_weekly":  pay_period_record_bi_weekly,
            "pay_period_record_weekly":  pay_period_record_weekly,
            "pay_period_record_hourly":  pay_period_record_hourly
        }
        return render(request, "business-view.html", data)

    return render(request, "business-view.html")

# fetch busienss records
def getBusinessRecords(user_id):
    # users
    user_record = users.objects.filter(id=user_id)
    # businesses
    business_record = businesses.objects.filter(user_id=user_id)

    # bank information
    business_ids = []
    for id in business_record:
        business_ids.append(id.id)
    

    print(business_ids)
    bank_details_record = []
    business_records = []
    for i in business_ids:
        bank_details_record.append(company_banking_details.objects.filter(business_id = i))
        business_records.append(businesses.objects.filter(id=i))

    payroll_records = []
    for n in business_ids:
        payroll_records.append(payroll.objects.filter(business_id=n))
    
    b_data = {
        "user_record": user_record,
        "bank_details_record": bank_details_record,
        "business_records": business_records,
        "payroll_records": payroll_records
    }

    return b_data
    # # print users record
    # for u in user_record:
    #     print('------------')
    #     print(u.id)
    #     print(u.first_name)
    #     print(u.last_name)
    #     print(u.email)
    #     print(u.mobile_number)
    #     print(u.password)
    #     print(u.account_type)
    #     print('--------------------')
    
    # # print business record
    # for b_record in business_records:
    #     for b in b_record:
    #         print('------------')
    #         print(b.id)
    #         print(b.business_name)
    #         print(b.street_1)
    #         print(b.street2)
    #         print(b.city)
    #         print(b.postal_code)
    #         print(b.parish)
    #         print(b.country)
    #         print(b.tax_registration_number)
    #         print(b.national_insurnce_scheme)
    #         print(b.business_start_date)
    #         print(b.user_id)
    #         print('----------------')
    
    # for bank_info_record in bank_details_record:
    #     for br in bank_info_record:
    #         print('-----------------')
    #         print(br.id)
    #         print(br.business_id)
    #         print(br.account_name)
    #         print(br.bank_name)
    #         print(br.branch)
    #         print(br.account_number)
    #         print(br.account_type)
    
    
    
