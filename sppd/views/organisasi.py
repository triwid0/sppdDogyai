from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from ..forms import *
from django.contrib import messages
from ..models import MasterOrganisasi
from django.utils import timezone
import os
from django.conf import settings
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# # Create your views here.
def index(request):
    title = 'Master Organisasi'
    page = request.GET.get('page', 1)
    organisasi= MasterOrganisasi.objects.all().order_by('id_organisasi').values()
    paginator = Paginator(organisasi, 200)
    try:
        organisasi = paginator.page(page)
    except PageNotAnInteger:
        organisasi = paginator.page(1)
    except EmptyPage:
        organisasi = paginator.page(paginator.num_pages)
    contex = {
        'title' : title,
        'data_organisasi' : organisasi
    }
    return render(request, 'master/master_organisasi/index.html', contex)

def permanentDelete(request, id):
    message = ''
    try:
        doc = MasterOrganisasi.objects.get(id_organisasi=id)
        doc.delete()
        message = 'success'
    except MasterOrganisasi.DoesNotExist:
        message = 'error'

    context = {
            'message' : message,
        }

    return HttpResponse(context)

def create(request):
    if request.method == 'POST':
        insert = MasterOrganisasi()
        kode_organisasi = request.POST.get('kode_organisasi')
        urai = request.POST.get('urai')
        if insert is not None:
            insert.kode_organisasi = kode_organisasi
            insert.urai = urai
            
            insert.save()
            
            messages.success(request, 'Kata Mereka berhasil disimpan.')
            return redirect('sppd:organisasi')

def edit(request, id):
    if request.method == 'POST':
        edit = MasterOrganisasi.objects.get(id_organisasi = id)
        Organisasi = request.POST['KodeEdit']
        urai = request.POST['uraiedit']
        
        if edit is not None:
                edit.kode_organisasi = Organisasi
                edit.urai = urai
                
                edit.save()

                messages.success(request, 'Kata Mereka berhasil disimpan.')
                return redirect('sppd:organisasi')

# def Off(request, id=""):
#     MasterJabatan.objects.filter(id=id).update(status = 0)
#     messages.success(request, 'Kata Mereka berhasil disimpan.')
#     return redirect('sppd:jabatan')

# def On(request, id=""):
#     MasterJabatan.objects.filter(id=id).update(status = 1)
#     messages.success(request, 'Kata Mereka berhasil disimpan.')
#     return redirect('sppd:jabatan')