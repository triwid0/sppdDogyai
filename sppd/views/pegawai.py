from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from ..forms import *
from django.contrib import messages
from ..models import MasterPegawai
from django.utils import timezone
import os
from django.conf import settings
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    title = 'MasterPegawai'
    page = request.GET.get('page', 1)
    pegawai = MasterPegawai.objects.all().order_by('id').values()
    paginator = Paginator(pegawai, 200)
    try:
        pegawai = paginator.page(page)
    except PageNotAnInteger:
        pegawai = paginator.page(1)
    except EmptyPage:
        pegawai = paginator.page(paginator.num_pages)
    contex = {
        'title' : title,
        'pegawai' : pegawai
    }
    return render(request, 'master/master_pegawai/index.html', contex)

def permanentDelete(request, id):
    message = ''
    try:
        doc = MasterPegawai.objects.get(id=id)
        try:
            doc.image.delete()
        except:
            pass
        doc.delete()
        message = 'success'
    except MasterPegawai.DoesNotExist:
        message = 'error'

    context = {
            'message' : message,
        }

    return HttpResponse(context)

def create(request):
    if request.method == 'POST':
        insert = MasterPegawai()
        nip = request.POST.get('nip')
        nama = request.POST.get('nama')
        golongan = request.POST.get('golongan')
        no_hp = request.POST.get('nohp')
        eselon = request.POST.get('eselon')
        alamat = request.POST.get('alamat')
        pangkat = request.POST.get('pangkat')
        email = request.POST.get('email')

        if insert is not None:
            insert.nip = nip
            insert.nama = nama
            insert.golongan = golongan
            insert.no_hp = no_hp
            insert.eselon = eselon
            insert.alamat = alamat
            insert.pangkat = pangkat
            insert.email = email

        insert.save()
            
        messages.success(request, 'Kata Mereka berhasil disimpan.')
        return redirect('sppd:pegawai')

def edit(request, id):
    if request.method == 'POST':
        edit = MasterPegawai.objects.get(id = id)
        nip = request.POST.get('nipedit')
        nama = request.POST.get('namaedit')
        golongan = request.POST.get('golonganedit')
        no_hp = request.POST.get('nohpedit')
        eselon = request.POST.get('eselonedit')
        alamat = request.POST.get('alamatedit')
        pangkat = request.POST.get('pangkatedit')
        email = request.POST.get('emailedit')
        
        if edit is not None:
                edit.nip = nip
                edit.nama = nama
                edit.no_hp = no_hp
                edit.golongan = golongan
                edit.eselon = eselon
                edit.alamat = alamat
                edit.pangkat = pangkat
                edit.email = email
                edit.save()

                messages.success(request, 'Kata Mereka berhasil disimpan.')
                return redirect('sppd:pegawai')

def Off(request, id=""):
    MasterPegawai.objects.filter(id=id).update(status = 0)
    messages.success(request, 'Kata Mereka berhasil disimpan.')
    return redirect('sppd:pegawai')

def On(request, id=""):
    MasterPegawai.objects.filter(id=id).update(status = 1)
    messages.success(request, 'Kata Mereka berhasil disimpan.')
    return redirect('sppd:pegawai')