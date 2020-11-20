from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from core import models

#Store Views
def store(request):
    return render(request, 'index.html')

def rateProduct(request):
    pass


#Cart Views
def cart(request):
    pass
def orderUpdate(request):
    pass
def checkout(request):
    pass
def processOrder(request):
    pass


#ADM Auth Views
def admLoginPage(request):
    pass
def admLoginSubmit(request):
    pass
def admLogout(request):
    pass
def admRegisterPage(request):
    pass
def admRegisterSubmit(request):
    pass

#Dashboard Views
def dashboard(request):
    pass
def orderDetails(request):
    pass

#Customers Views
def customersADMPage(request):
    pass
def customersADMPageFilter(request):
    pass
def customerInfoPage(request):
    pass
def customerProfilePage(request):
    pass

#Products Views
def productPage(request):
    pass
def productSubmit(request):
    pass


#Stock Views
def stockPage(request):
    pass
def stockPageFilter(request):
    pass


#Customer Login Views
def customerLoginPage(request):
    pass
def customerLoginSubmit(request):
    pass
def customerLogout(request):
    pass
def customereRegisterSubmit(request):
    pass
def customerRegister(request):
    pass

