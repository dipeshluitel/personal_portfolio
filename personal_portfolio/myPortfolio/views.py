from django.shortcuts import render
from myPortfolio.forms import GuestForm

# Create your views here.
def index(request):
    return render(request,'myPortfolio/index.html')

def about(request):
    return render(request,'myPortfolio/about_me.html')


def project(request):
    return render(request,'myPortfolio/projects.html')

def contact(request):
    contacted = False

    if request.method == "POST":
        guest_form = GuestForm(data=request.POST)

        if guest_form.is_valid():
            guest = guest_form.save()
            guest.save()

            contacted = True
        else:
            print(guest_form.errors)
    
    else:
        guest_form = GuestForm()

    return render(request,'myPortfolio/contact.html', {'guest_form':guest_form})
