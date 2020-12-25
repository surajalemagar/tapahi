from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.urls import reverse, reverse_lazy
from verifytapahi.models import OrderCodeNumber

n= OrderCodeNumber.objects.all()


def Home(request):
    return render(request, 'home.html')


def Check(request):
    
    try:
        a = int(request.POST['order_number1'])
        b = int(request.POST['code1'])
    except:
        return render(request, 'wrong.html')
    
    if a<1001:
        if n[a].code==b:
            return render(request, 'success.html')
        else:
            return render(request, 'wrong.html')
    else:
        return render(request, 'wrong.html')
