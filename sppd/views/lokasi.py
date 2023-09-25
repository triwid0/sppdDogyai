from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from ..forms import *
from django.contrib import messages
from ..models import MasterLokasi
from django.utils import timezone
import os
from django.conf import settings
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    title = 'MasterLokasi'
    page = request.GET.get('page', 1)
    lokasi = MasterLokasi.objects.all().order_by('id').values()
    paginator = Paginator(lokasi, 200)
    try:
        lokasi = paginator.page(page)
    except PageNotAnInteger:
        lokasi = paginator.page(1)
    except EmptyPage:
        lokasi = paginator.page(paginator.num_pages)
    contex = {
        'title' : title,
        'lokasi' : lokasi
    }
    return render(request, 'master/master_lokasi/index.html', contex)

def permanentDelete(request, id):
    message = ''
    try:
        doc = MasterLokasi.objects.get(id=id)
        try:
            doc.image.delete()
        except:
            pass
        doc.delete()
        message = 'success'
    except MasterLokasi.DoesNotExist:
        message = 'error'

    context = {
            'message' : message,
        }

    return HttpResponse(context)

def create(request):
    if request.method == 'POST':
        insert = MasterLokasi()
        kd_lokasi = request.POST.get('kd_lokasi')
        urai   = request.POST.get('urai')
        if insert is not None:
            insert.kd_lokasi = kd_lokasi
            insert.urai = urai
            insert.save()
            
            messages.success(request, 'Kata Mereka berhasil disimpan.')
            return redirect('sppd:lokasi')

def edit(request, id):
    if request.method == 'POST':
        edit = MasterLokasi.objects.get(id = id)
        kd_lokasi = request.POST['kd_lokEdit']
        urai = request.POST['uraiEdit']
        if edit is not None:
                edit.kd_lokasi = kd_lokasi
                edit.urai = urai
                edit.save()

                messages.success(request, 'Kata Mereka berhasil disimpan.')
                return redirect('sppd:lokasi')

def Off(request, id=""):
    MasterLokasi.objects.filter(id=id).update(status = 0)
    messages.success(request, 'Kata Mereka berhasil disimpan.')
    return redirect('sppd:lokasi')

def On(request, id=""):
    MasterLokasi.objects.filter(id=id).update(status = 1)
    messages.success(request, 'Kata Mereka berhasil disimpan.')
    return redirect('sppd:lokasi')