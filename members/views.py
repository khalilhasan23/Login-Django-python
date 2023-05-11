from django.shortcuts import render, redirect
from .models  import Accounts


# Create your views here.

def members(request):


    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        password = request.POST.get("password")
        email =  request.POST.get("email")
        city =  request.POST.get("city")
        zip =  request.POST.get("zip")
        address =  request.POST.get("address")

        data = Accounts(fname=fname,lname=lname,password=password,email=email
                        , city=city,  zip=zip, address= address)

        data.save()
        return redirect('login')


    return render(request, 'members/index.html')



def login(request):

    if request.method == 'POST':

        password = request.POST.get("password")
        email =  request.POST.get("email")

        x= Accounts.objects.all()

        for i in x  :
            if i.email == email:
                if i.password == password:
                    return redirect('members')


        return redirect('wrong')
    
    return render(request, 'login/login.html')


def wrong(req):
    return render(req, 'members/wrong.html')