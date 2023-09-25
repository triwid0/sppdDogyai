from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from ..forms import *
from django.contrib import messages
from ..models import MasterJabatan
from django.utils import timezone
import os
from django.conf import settings
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# # Create your views here.
def index(request):
    title = 'Master Jabatan'
    page = request.GET.get('page', 1)
    jabatan = MasterJabatan.objects.all().order_by('id').values()
    paginator = Paginator(jabatan, 200)
    try:
        jabatan = paginator.page(page)
    except PageNotAnInteger:
        jabatan = paginator.page(1)
    except EmptyPage:
        jabatan = paginator.page(paginator.num_pages)
    contex = {
        'title' : title,
        'jabatan' : jabatan
    }
    return render(request, 'master/master_jabatan/index.html', contex)

def permanentDelete(request, id):
    message = ''
    try:
        doc = MasterJabatan.objects.get(id=id)
        doc.delete()
        message = 'success'
    except MasterJabatan.DoesNotExist:
        message = 'error'

    context = {
            'message' : message,
        }

    return HttpResponse(context)

def create(request):
    if request.method == 'POST':
        insert = MasterJabatan()
        jabatan = request.POST.get('jabatan')
        if insert is not None:
            insert.jabatan = jabatan
            insert.save()
            
            messages.success(request, 'Kata Mereka berhasil disimpan.')
            return redirect('sppd:jabatan')

def edit(request, id):
    if request.method == 'POST':
        edit = MasterJabatan.objects.get(id = id)
        jabatan = request.POST['jbtEdit']
        if edit is not None:
                edit.jabatan = jabatan
                edit.save()

                messages.success(request, 'Kata Mereka berhasil disimpan.')
                return redirect('sppd:jabatan')

def Off(request, id=""):
    MasterJabatan.objects.filter(id=id).update(status = 0)
    messages.success(request, 'Kata Mereka berhasil disimpan.')
    return redirect('sppd:jabatan')

def On(request, id=""):
    MasterJabatan.objects.filter(id=id).update(status = 1)
    messages.success(request, 'Kata Mereka berhasil disimpan.')
    return redirect('sppd:jabatan')