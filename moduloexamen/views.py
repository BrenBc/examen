from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import *
from django.db.models import Sum

# Create your views here.

def home (request):
    productos = Producto.objects.all()


    contexto = {'productos':productos}
    return render(request, 'moduloexamen/home.html', contexto)
