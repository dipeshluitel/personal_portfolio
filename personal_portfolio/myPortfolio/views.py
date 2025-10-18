from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'myPortfolio/index.html')

def about(request):
    return render(request,'myPortfolio/about_me.html')


def projects(request):
    return render(request,'myPortfolio/projects..html')

def contact(request):
    contacted = False


    return render(request,'myPortfolio/contact.html')