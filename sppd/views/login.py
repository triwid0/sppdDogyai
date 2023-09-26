from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from ..forms import *
from django.contrib import messages
from ..models import Account
from django.utils import timezone
import os
from django.conf import settings
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password





def loginUser(request):

    if request.method == 'GET':
        contex = {
            'title' : 'Login'
        }   
        return render(request, 'auth/index.html', contex)
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('sppd:dash')
        else:
            return redirect('sppd:login')


def addUser(request):
    contex = {
        'title' : 'Add User'
    }

    if request.method == "POST":
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        password = request.POST.get('password')

        insert = Account()
        insert.email = email
        insert.nama = nama
        insert.set_password(password)
        insert.save()

        return redirect('sppd:login')

    return render(request, 'auth/addUser.html', contex)