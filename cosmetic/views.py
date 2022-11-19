from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.db.models import Max
from django.db import connection
from .models import *
import json
import re

# Create your views here.
def index(request):
    data = {}
    return render(request, 'index.html', data)

def signup(request):
    data = {}
    return render(request, 'sign_up.html', data)

def signin(request):
    data ={}
    return render(request, 'sign_in.html', data)

def Promotion(request):
    data = {}
    return render(request, 'promotion.html', data)

def lipstick(request):
    data={}
    return render(request, 'lipstick.html', data)

def eyeLiner(request):
    data={}
    return render(request, 'eyeliner.html', data)

def mascara(request):
    data={}
    return render(request, 'mascara.html', data)

def eyebrownpencil(request):
    data={}
    return render(request, 'eyebrown_pencil.html', data)

def powderpuff(request):
    data={}
    return render(request, 'powder_puff.html', data)

def foundation(request):
    data={}
    return render(request, 'foundation.html', data)

def gucci(request):
    data= {}
    return render(request, 'gucci.html', data)

def Payment(request):
    data = {}
    return render(request, 'payment.html', data)

class customerlist(View):
    def get(self, request):
        customers = list(customer.objects.all().values())
        data = dict()
        data['customers'] = customers

        return JsonResponse(data)

class productlist(View):
    def get(self, request):
        products = list(product.objects.all().values())
        data = dict()
        data['products'] = products

        return JsonResponse(data)


