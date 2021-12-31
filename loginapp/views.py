from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.models import User
from seller.models import bidding, seller
from datetime import datetime
from django.db.models import Max, aggregates
def selectview(request):
    return render(request,'select.html')

# Create your views here.
def loginview(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["upass"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(selectview)
    return render(request,'login.html')
# def mainloginview(request):
#     return render(request, 'mainlogin.html')
def logoutview(request):
    logout(request)
    return redirect(loginview)
    # return render(request,'logout.html')
def signupview(request):
    if request.method=="POST":
        username=request.POST["uname"]
        email=request.POST["uemail"]
        password=request.POST["upass"]
        cpassword=request.POST["ucpass"]
        if password!=cpassword:
            return render(request,'signup.html')
        else:
            try:
                va=User.objects.get(username=username)
                return render(request,'signup.html',{'register':'User already exist'})
            except:
                user = User.objects.create_user(username,email,password)
                user.save()
                return render(request,'login.html')

    return render(request,'signup.html')
    
def contactusview(request):
    return render(request,'contact.html')

def sellerview(request):
    if request.method == "POST":
        productname = request.POST["productname"]
        productprice = request.POST["productprice"]
        deadline = request.POST["deadline"]
        productimage = request.POST["productimage"]
        print(productimage)
        object1 = seller(productname = productname,productprice=productprice,deadline =deadline,productimage = productimage)
        object1.save()
        return render(request,'select.html',{'register':'Product Added Successfully!!!'})
    return render(request, 'seller.html')
        # fetch all the details and add it to the seller table
        # return render(request, 'mainlogin.html')

def bidderview(request):
    objects = seller.objects.all()
    timenotdone = []  
    date1 = datetime.today().strftime("%B %d, %Y")
    time1 = datetime.today().strftime("%H:%M:%S")
    for x in objects:
        date2 = x.deadline.strftime("%B %d, %Y")
        if date1>=date2:
            if date1==date2:
                time2 = x.deadline.strftime("%H:%M:%S")
                if time1<time2:
                    timenotdone.append(x)
        else:
            timenotdone.append(x)
    # print(timedone)
    return render(request, 'bidder.html',{'objects':timenotdone})

def biddingview(request,objectid):
    object1 = seller.objects.get(id=objectid)
    if request.method == "POST":
        amount = request.POST["amount"]
        if int(amount) < object1.productprice:
            return render(request,'bidding.html',{'object1':object1,'register':"Bid Value must be greater than "+str(object1.productprice)})
        else:
            try:
                isobject = bidding.objects.get(userid = request.user,productid = objectid)
                isobject.bidamount = amount
                isobject.save()
            except:
                object2 = bidding(userid = request.user,productid = object1,bidamount = amount)
                object2.save()
            objects = seller.objects.all()
            timenotdone = []  
            date1 = datetime.today().strftime("%B %d, %Y")
            time1 = datetime.today().strftime("%H:%M:%S")
            for x in objects:
                date2 = x.deadline.strftime("%B %d, %Y")
                if date1>=date2:
                    if date1==date2:
                        time2 = x.deadline.strftime("%H:%M:%S")
                        if time1<time2:
                            timenotdone.append(x)
                else:
                    timenotdone.append(x)
            return render(request, 'bidder.html',{'objects':timenotdone,'register':"Bidding Completed Successfully!!!"})
    return render(request,'bidding.html',{'object1':object1})

def announcementview(request):
    objects = seller.objects.all()
    date1 = datetime.today().strftime("%B %d, %Y")
    time1 = datetime.today().strftime("%H:%M:%S")
    timedone = []
    for x in objects:
        date2 = x.deadline.strftime("%B %d, %Y")
        if date1>=date2:
            if date1==date2:
                time2 = x.deadline.strftime("%H:%M:%S")
                if time1>=time2:
                    timedone.append(x)
            else:
                timedone.append(x)
    persons = []
    for x in timedone:
        list1_id = []
        list2_bidamount = []
        objects_bid = bidding.objects.filter(productid = x)
        for i in objects_bid:
            list1_id.append(i)
            list2_bidamount.append(i.bidamount)
        print(list2_bidamount)
        if len(list2_bidamount)!=0:
            maxamountbid = max(list2_bidamount)
            index = list2_bidamount.index(maxamountbid)
            person_bid_max = list1_id[index]
            persons.append(person_bid_max)
    if len(persons) == 0:
        return render(request,'announcement.html',{'register':"No item Has Finished Deadline to announce the result"})
    return render(request,'announcement.html',{'objects':persons})