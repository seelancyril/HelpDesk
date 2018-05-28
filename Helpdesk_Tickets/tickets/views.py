from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def homePage(request):
	return render(request, 'tickets/HomePage.html', {'status':'Working'})

def newTicket(request):
	return render(request, 'tickets/NewTicket.html', {'status':'Working'})