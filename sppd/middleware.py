from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .helpers import *
from .models.sppd import LogAdmin, LogVisitor
from datetime import *
from django.utils.timezone import localtime

# MIDDLEWARE UNTUK MENCATAT LOG PENGGUNA
def log_visitor(get_response):

    # One-time configuration and initialization.
    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        if request.path[0:29].lower() =='/' or request.path[0:29].lower() not in '/manage_panel' or request.path[0:29].lower() not in '/sudo_manage_panel':
            try:
                user_info = get_user_info(request)
                last_log =  LogVisitor.objects.filter(ip=user_info['ip']).latest('waktu')
                time_db = datetime.strptime(str(localtime(last_log.waktu)).split('+')[0], '%Y-%m-%d %H:%M:%S.%f')
                time_now = datetime.now()
                time_selisih_menit = (time_now - time_db).total_seconds()/60
                if int(time_selisih_menit) > 20:
                    insert_log_visitor(request)
            except:
                insert_log_visitor(request)

        return response

    return middleware