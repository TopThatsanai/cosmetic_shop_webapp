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


