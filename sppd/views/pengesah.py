from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from ..forms import *
from django.contrib import messages
from ..models import MasterPengesah
from ..models import MasterPegawai
from ..models import MasterJabatan
from django.utils import timezone
import os
from django.conf import settings
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    title = 'MasterPegawai'
    page = request.GET.get('page', 1)
    pengesah = MasterPengesah.objects.select_related('jabatan', 'pegawai').all()
    pegawai = MasterPegawai.objects.all().order_by('id').values()
    jabatan = MasterJabatan.objects.all().order_by('id').values()
    
    paginator = Paginator(pengesah, 200)
    try:
        pengesah = paginator.page(page)
    except PageNotAnInteger:
        pengesah = paginator.page(1)
    except EmptyPage:
        pengesah = paginator.page(paginator.num_pages)
    contex = {
        'title' : title,
        'pengesah' : pengesah,
        'pegawai' : pegawai,
        'jabatan' : jabatan,
    }
    return render(request, 'master/master_pengesah/index.html', contex)

def permanentDelete(request, id):
    message = ''
    try:
        doc = MasterPengesah.objects.get(id=id)
        try:
            doc.image.delete()
        except:
            pass
        doc.delete()
        message = 'success'
    except MasterPengesah.DoesNotExist:
        message = 'error'

    context = {
            'message' : message,
        }

    return HttpResponse(context)

def create(request):
    if request.method == 'POST':
        insert = MasterPengesah()
        id_pegawai = request.POST.get('pegawai')
        id_jabatan = request.POST.get('jabatan')
        no_rek = request.POST.get('no_rek')
        nama_bank = request.POST.get('nama_bank')
        if insert is not None:
            insert.pegawai_id = id_pegawai
            insert.jabatan_id = id_jabatan
            insert.no_rek = no_rek
            insert.nama_bank = nama_bank

        insert.save()
            
        messages.success(request, 'Kata Mereka berhasil disimpan.')
        return redirect('sppd:pengesah')

def edit(request, id):
    if request.method == 'POST':
        edit = MasterPengesah.objects.get(id = id)
        pegawai_id = request.POST.get('pegawai')
        jabatan_id = request.POST.get('jabatan')
        no_rek = request.POST.get('no_rek')
        nama_bank = request.POST.get('nama_bank')
        
        if edit is not None:
                edit.pegawai_id = pegawai_id
                edit.jabatan_id = jabatan_id
                edit.no_rek = no_rek
                edit.nama_bank = nama_bank
                
                edit.save()

                messages.success(request, 'Kata Mereka berhasil disimpan.')
                return redirect('sppd:pengesah')

def Off(request, id=""):
    MasterPengesah.objects.filter(id=id).update(status = 0)
    messages.success(request, 'Kata Mereka berhasil disimpan.')
    return redirect('sppd:pengesah')

def On(request, id=""):
    MasterPengesah.objects.filter(id=id).update(status = 1)
    messages.success(request, 'Kata Mereka berhasil disimpan.')
    return redirect('sppd:pengesah')