import os

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from django.contrib.gis.geoip2.resources import City
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, request
from rest_framework import permissions, status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView


from emailapp import models
from django import forms
from django.core.files.storage import FileSystemStorage

from .forms import SetProfileForm
from .models import getprofileData
from .models import signUp
from django.db.models import Q
from django import forms
from rest_framework.decorators import api_view






class loginPageView(TemplateView):

    template_name = 'emailapp/index.html'

class homePageView(TemplateView):
    template_name = 'emailapp/home.html'

def inbox(request):
    mail = models.receiveMsg.objects.all
    return render(request, "emailapp/home", { "obj":mail })

def homePage(request):
    receivedData = models.receiveMsg.objects.filter(cruser=userName)
    temp = 0
    email = request.GET.get("search")
    print(email)
    try:
        person_obj = models.usersLog.objects.get(usmail=userName)
    except models.usersLog.DoesNotExist:
        usdata = models.usersLog(usmail=userName)
        usdata.save()

    if request.method == "POST":
        sendmail      =  request.POST["sendmail"]
        sendsubject   =  request.POST["sendsubject"]
        sendtext      =  request.POST["sendtext"]
        print(sendmail, sendsubject, sendtext)
        savedata = models.sendMsg(cruser=userName,sendmail=sendmail , sendsubject = sendsubject , sendtext = sendtext)
        savedata.save()
    if request.method.lower() == "get" and email != None:
        email = request.GET.get("search")
        template_name = "home.html"
        print(email)
        object_list = models.receiveMsg.objects.filter(
            Q(cruser__icontains=userName) | Q(cruser__icontains=userName)
        )
        email=None
        return render(request, 'emailapp/home.html', {"obj": object_list})





    return render(request,'emailapp/home.html',{"obj":receivedData})

def homeSearch(request):
    receivedData = models.receiveMsg.objects.all
    if request.method == "GET":
        template_name = "home.html"
        email = request.GET.get("Hsearch")
        query = request.GET.get("search")
        print(email)


        object_list = models.receiveMsg.objects.filter(
            Q(receivemail__icontains=email) | Q(receivemail__icontains=email)
        )
        return render(request, 'emailapp/homeSearch.html', {"obj": object_list})

    return render(request, 'emailapp/homeSearch.html', {"obj": receivedData})

def login(request):

    global userName

    model = models.signUp
    template_name = "index.html"
    print(request)
    signin = False
    user = request.GET.get("user_name")
    userName = user

    password = request.GET.get("password")
    print(user,password)

    if request.method == "GET":
        t=0

        if user==None:
            user="test@gmail.com"
        try:
            person_obj = models.signUp.objects.get(semail=user)
        except models.usersLog.DoesNotExist:
            return render(request, "emailapp/index.html")
        if person_obj.semail == user and person_obj.spass == password:
            user=None
            password=None
            t=1
            return render(request, "emailapp/home.html")
        else:
            t ==0
            t=1
            return render(request,"emailapp/retry.html")


    return render(request,"emailapp/index.html")


def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        semail   = request.POST['semail']
        spass    = request.POST['spass']
        srpass   = request.POST['srpass']
        print( username ,semail,spass,srpass)
        if srpass == spass:
            try:

                person_obj = models.signUp.objects.get(username=username)
            except models.setContacts.DoesNotExist:
                savedata = models.signUp(username=username, semail=semail, spass=spass, srpass=srpass)
                savedata.save()
                print("saved data to database")
                return render(request, 'emailapp/index.html')
            return render(request, "emailapp/updateContacts.html")




    return render(request, 'emailapp/signUp.html')

def getdata(request):
    if request.method =="POST":
        name = request.POST['name']
        print(name)
    return render(request,'emailapp/getdata.html')

def show_data(request):
    data = models.sendMsg.objects.filter(cruser=userName)
    return render(request,"emailapp/showData.html",{"obj":data})

def searchMails(request):
    return render(request, "emailapp/sd.html")


# Create your views here.
def SearchResultsView(request):
    model = models.signUp
    template_name = "sd.html"
    print(request)
    query = request.GET.get("q")
    signin = False

    if request.method == "GET":
        object_list = models.signUp.objects.filter(
            Q(username__icontains=query) | Q(semail__icontains=query)
        )
        for values in object_list:
            if query == values.username:
                b=True
                return render(request, "emailapp/index.html")

def SearchHome(request):
    mail = request.GET.get["getSE"]
    maildata = models.receiveMsg.objects.filter(
        Q(receivemail__icontains=mail)
    )

    return render(request, "emailapp/home.html" , {"obj":maildata})

class setProfilePages(ListView):
    model = getprofileData
    template_name = "emailapp/displayProfile.html"


class showProfile(ListView):  # new
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']


def profilePage(request):
    if request.method == "a":
        data = models.getprofileData(request.POST ,request.FILES)
        fs = FileSystemStorage()
        data
        if data.is_valid():
            data.save()
        choosefile = request.FILES['choosefile']
        pname = request.POST["pname"]
        pmail = request.POST["pmail"]
        pdate = request.POST["pdate"]
        pcountry = request.POST["pcountry"]
        paddress = request.POST["paddress"]
        pnumber = request.POST["pnumber"]
        pprofession = request.POST["pprofession"]
        ppass = request.POST["ppass"]
        prpass = request.POST["prpass"]
        pid = request.FILES["pid"]
        #savedata = models.profileData( pname=pname, pmail=pmail, pdate=pdate, pcountry=pcountry, paddress=paddress, pnumber=pnumber, pprofession=pprofession, ppass=ppass, prpass=prpass)
        #savedata.save()
        data.save()

    if request.method == 'POST':
        model = models.getprofileData
        template_name = "profile.html"
        form = SetProfileForm(request.POST, request.FILES)
        pname = request.POST["pname"]
        pmail = request.POST["pmail"]
        pdate = request.POST["pdate"]
        pcountry = request.POST["pcountry"]
        paddress = request.POST["paddress"]
        pnumber = request.POST["pnumber"]
        pprofession = request.POST["pprofession"]
        ppass = request.POST["ppass"]
        prpass = request.POST["prpass"]
        print(form.is_valid())
        #savedata = models.profileData(pname=pname, pmail=pmail, pdate=pdate, pcountry=pcountry, paddress=paddress, pnumber=pnumber, pprofession=pprofession, ppass=ppass, prpass=prpass)
        #savedata.save()


        if form.is_valid():
            form.save()
            print('success')
            data = form.instance
            userProfile = models.getprofileData.objects.filter(pname=request.user)
            context = {
                'form': form,
                'obj': userProfile
            }
            return render(request, 'emailapp/displayProfile.html', context)
            #return render(request, 'emailapp/displayProfile.html', {'form':form,'obj':data})
    else:
        form = SetProfileForm()

    return render(request,"emailapp/profile.html")

def forgotPassword(request):
    if request.method == "POST":
        pasw = request.POST.get("fpass")
        rpasw = request.POST.get("frpass")
        if pasw == rpasw:
            models.signUp.objects.filter(semail=forgotenMail).update(spass=pasw)
            render(request, "emailapp/index.html")
        else:
            render(request, "emailapp/PasswordCreationFailed.html")

    return render(request, "emailapp/forgotPassword.html")
def forgotMail(request):
    global forgotenMail
    template_name = "forgotEmail.html"
    mail = request.GET.get("frmail")
    forgotenMail = mail
    print(forgotenMail)
    try:
        person_obj = models.signUp.objects.get(semail=mail)
    except models.signUp.DoesNotExist:
        return render(request, "emailapp/forgotEmail.html")

    return render(request, "emailapp/forgotPassword.html")

def contactsPage(request):
    return render(request, "emailapp/getContacts.html")

def addcontactsPage(request):
    if request.method == "POST":
        cusername = request.POST['cusername']
        cemail    = request.POST['cemail']
        cphonenumber = request.POST['cphonenumber']
        caddress = request.POST['caddress']
        #,cphonenumber=cphonenumber, caddress=caddress


        print(cusername,cemail)
        savedata = models.setContacts(cemailholder=userName,cusername=cusername,cemail=cemail ,cphonenumber=cphonenumber, caddress=caddress)
        savedata.save()

    return render(request, "emailapp/contacts.html")

def deletecontactsPage(request):
    if request.method == "POST":
        user = request.POST["dusername"]
        mail = request.POST["demail"]
        object_list = models.setContacts.objects.filter(
            Q(cusername__icontains=user) & Q(cemail__icontains=mail)
        )
        object_list.delete()


    return render(request, "emailapp/deleteContacts.html")

def updatecontactsPage(request):
    template_name="updateContacts.html"
    model = models.setContacts

    name = request.POST.get("uusername")
    mail = request.POST.get("uemail")
    print(name)
    print(mail)
    try:
        person_obj = models.setContacts.objects.get(cusername=name)
    except models.setContacts.DoesNotExist:
        return render(request, "emailapp/updateContacts.html")
    models.setContacts.objects.filter(cusername=name).update(cemail=mail)

    return render(request, "emailapp/updateContacts.html")

def displaycontactsPage(request):
    data = models.setContacts.objects.filter(cemailholder=userName)

    return render(request, "emailapp/displayContacts.html", {"obj": data})


def fullContact(request):
    name = request.GET.get("csearch")
    if request.method.lower() == "get" and name != None:
        name = request.GET.get("csearch")
        template_name = "fullContactDetails.html"
        print(name)
        object_list = models.setContacts.objects.filter(
            Q(cusername__icontains=name) & Q(cemailholder__icontains=userName)
        )

        return render(request, 'emailapp/fullContactDetails.html', {"obj": object_list})

    return render(request,"emailapp/fullContactDetails.html")



def displayProfile(request):
    form = SetProfileForm(request.POST ,request.FILES)
    print(userName)
    userProfile = models.getprofileData.objects.filter(pmail=userName)
    context = {
        'form': form,
        'obj': userProfile
    }



    return render(request, 'emailapp/getProfile.html', context)

    #print(data.instance.pname)
    #print("profile")

    #return render(request, "emailapp/displayProfile.html", {"obj": data})



def updateProfile(request):

    if request.method == "GET":
        form = SetProfileForm(request.POST, request.FILES)
        print(userName)
        userProfile = models.getprofileData.objects.filter(pmail=userName)
        context = {
            'form': form,
            'obj': userProfile
        }

        return render(request, 'emailapp/editProfile.html', context)
    if request.method == "POST":
        pname = request.POST.get("pname")
        pmail = request.POST.get("pmail")
        pdate = request.POST.get("pdate")
        pcountry = request.POST.get("pcountry")
        paddress = request.POST.get("paddress")
        pnumber = request.POST.get("pnumber")
        pprofession = request.POST.get("pprofession")
        ppass = request.POST.get("ppass")
        prpass = request.POST.get("prpass")
        models.getprofileData.objects.filter(pmail=userName).update(pname=pname, pmail=pmail,  pcountry=pcountry, paddress=paddress, pnumber=pnumber, pprofession=pprofession, ppass=ppass, prpass=prpass)
        return render(request, 'emailapp/editProfile.html')



def uploadFile(request):
    geturl = {}

    if request.method == "POST":

        img = request.FILES['uploadfiles']
        print(img.name)
        print(img.size)
        fs = FileSystemStorage()
        name = fs.save(img.name,img)
        geturl['url'] = fs.url(name)
        localAddr =  os.getcwd()
        print(fs.url(name))
        print(localAddr)
    return render(request, 'emailapp/uploadFile.html',geturl)







def sum1(request):
    num1 = int(request.GET['first1'])
    num2 = int(request.GET['second1'])
    result = num1 + num2
    return render(request, 'sd.html', {'result':result})


def updateLogin(request):
    pasw =  request.POST["fpass"]
    rpasw = request.POST["frpass"]
    if pasw == rpasw:
        models.login.objects.filter(pmail=userName).update(password=pasw)
        render(request,"emailapp/createdNewPassword.html")
    else:
        render(request, "emailapp/PasswordCreationFailed.html")

def userLogPage(request):
    object_list = models.usersLog.objects.filter(
        ~Q(usmail__icontains = userName) | ~Q(usmail__icontains=userName)
    )
    return render(request, 'emailapp/displayUserlogs.html', {'obj': object_list})

def sendedMessages(request):
    object = models.sendMsg.objects.filter(cruser=userName)
    return render(request, 'emailapp/sentMailPage.html', {'obj': object})
def wallerPage(request):
    data = models.walletBalance.objects.filter(id = 1)
    return render(request, 'emailapp/wallet.html',{'obj':data})


def loggedOutPage(request):
    return render(request,'emailapp/loggedOut.html')

def retryPage(request):
    return render(request, 'emailapp/retry.html')

def addWalletBal(request):
    if request.method == "POST":
        m = request.POST.get("addbal")
        dt = models.walletBalance.objects.filter(id=1)
        sum=0
        print(m)
        if m == None:
            m="0"
        for items in dt:
            sum = int(m)+int(items.wallet)
            m=None

        data = models.walletBalance.objects.filter(id=1).update(wallet=sum)
    return render(request, 'emailapp/addWalletBalance.html')