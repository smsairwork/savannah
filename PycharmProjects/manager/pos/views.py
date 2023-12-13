from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def services(request):
    return render(request, 'services.html')


def team(request):
    return render(request, 'team.html')

def next(request):
    return render(request, 'Next Team.html')

def client(request):
    return render(request, 'client.html')

def home(request):
    return render(request, 'home.html')

def info(request):
    return render(request, 'info.html')

def address(request):
    return render(request, 'our address.html')

def other(request):
    return render(request, 'other services.html')


