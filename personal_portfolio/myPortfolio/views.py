from django.shortcuts import render,redirect
from myPortfolio.forms import GuestForm
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'myPortfolio/index.html',{'current_year':datetime.now().year})

def about(request):
    return render(request,'myPortfolio/about_me.html',{'current_year':datetime.now().year})


def project(request):
    return render(request,'myPortfolio/projects.html',{'current_year':datetime.now().year})

def contact(request):
    contacted = False

    if request.method == "POST":
        guest_form = GuestForm(data=request.POST)

        if guest_form.is_valid():
            guest = guest_form.save()
            guest.save()

            contacted = True
            redirect('modal')
        else:
            print(guest_form.errors)
    
    else:
        guest_form = GuestForm()

    return render(request,'myPortfolio/contact.html', {'guest_form':guest_form,'current_year':datetime.now().year})
