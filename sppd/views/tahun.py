from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from ..forms import *
from django.contrib import messages
from ..models import MasterTahun
from django.utils import timezone
import os
from django.conf import settings
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def index(request):
#     page = request.GET.get('page', 1)
#     news = Kata.objects.filter(deleted_at__isnull=True).order_by('-created_at', )
#     archives = Kata.objects.filter(deleted_at__isnull=False).order_by('-created_at')
#     paginator = Paginator(news, 15)
#     try:
#         news = paginator.page(page)
#     except PageNotAnInteger:
#         news = paginator.page(1)
#     except EmptyPage:
#         news = paginator.page(paginator.num_pages)

#     context = {
#         'title' : 'Kata Mereka - Admin',
#         'newss' : news,
#         'archives' : archives,
#     }
    
#     return render(request, 'profile/admin/kata/index.html', context)

# @login_required
# @is_verified()
# def create(request):
#     template = ''
#     context = {} 
#     form = ''

#     if request.method == 'GET':
#         form = Kata.objects.all()
#         context = {
#             'title' : 'ADD KATA MEREKA',
#             'form' : form,
#         }

#         template = 'profile/admin/kata/create.html'
#         return render(request, template, context)
    
#     if request.method == 'POST':
#         image = request.FILES['image']
#         judul = request.POST.get('judul')
#         keterangan = request.POST.get('keterangan')
#         if judul is not None:
#             new_news = Kata()
#             new_news.image = image
#             new_news.judul = judul
#             new_news.keterangan = keterangan
#             new_news.save()
            
#             messages.success(request, 'Kata Mereka berhasil disimpan.')
#             return redirect('profile:admin_KM')

#         messages.error(request, 'Kata Mereka gagal disimpan.')
#         return render(request, 'profile/admin/kata/create.html', {'form': form,})
    
# @login_required
# @is_verified()
# def edit(request, id):
#     template = ''
#     context = {} 
#     form = ''
    
#     if request.method == 'GET':
#         news = Kata.objects.get(id = id)

#         context = {
#             'title' : 'EDIT KATA MEREKA',
#             'form' : form,
#             'edit' : 'true',
#             'news' : news,
#         }
#         template = 'profile/admin/kata/create.html'
#         return render(request, template, context)
    
#     if request.method == 'POST':
#         news = Kata.objects.get(id = id)
#         path_file_lama = f"{settings.MEDIA_ROOT}/{news.image}"
#         foto_old = bool(news.image)
#         judul = request.POST.get('judul')
#         keterangan = request.POST.get('keterangan')

#         if news is not None:
#             news.judul = judul
#             news.keterangan = keterangan
#             news.save()
    
#             if 'image' in request.FILES:
#                 if foto_old : 
#                     try:
#                         os.remove(path_file_lama)
#                     except:
#                         pass
#                 foto = request.FILES['image']
#                 news.image = foto
#                 news.save()

#             messages.success(request, 'Kata Mereka berhasil disimpan')
#             return redirect('profile:admin_KM')

#         messages.error(request, 'Kata Mereka gagal disimpan.')
#         return render(request, 'profile/admin/kata/create.html', {'form': form,})

# # Create your views here.
def index(request):
    title = 'MasterTahun'
    page = request.GET.get('page', 1)
    tahun = MasterTahun.objects.all().order_by('id').values()
    paginator = Paginator(tahun, 200)
    try:
        tahun = paginator.page(page)
    except PageNotAnInteger:
        tahun = paginator.page(1)
    except EmptyPage:
        tahun = paginator.page(paginator.num_pages)
    contex = {
        'title' : title,
        'tahun' : tahun
    }
    return render(request, 'master/master_tahun/index.html', contex)

def permanentDelete(request, id):
    message = ''
    try:
        doc = MasterTahun.objects.get(id=id)
        try:
            doc.image.delete()
        except:
            pass
        doc.delete()
        message = 'success'
    except MasterTahun.DoesNotExist:
        message = 'error'

    context = {
            'message' : message,
        }

    return HttpResponse(context)

def create(request):
    if request.method == 'POST':
        insert = MasterTahun()
        tahun = request.POST.get('tahun')
        if insert is not None:
            insert.tahun = tahun
            insert.save()
            
            messages.success(request, 'Kata Mereka berhasil disimpan.')
            return redirect('sppd:tahun')

def edit(request, id):
    if request.method == 'POST':
        edit = MasterTahun.objects.get(id = id)
        tahun = request.POST['thnEdit']
        if edit is not None:
                edit.tahun = tahun
                edit.save()

                messages.success(request, 'Kata Mereka berhasil disimpan.')
                return redirect('sppd:tahun')

def Off(request, id=""):
    MasterTahun.objects.filter(id=id).update(status = 0)
    messages.success(request, 'Kata Mereka berhasil disimpan.')
    return redirect('sppd:tahun')

def On(request, id=""):
    MasterTahun.objects.filter(id=id).update(status = 1)
    messages.success(request, 'Kata Mereka berhasil disimpan.')
    return redirect('sppd:tahun')
# def addTahun(request):
#     if request.method == "POST":
#         tahun = request.POST.get('tahun')

#         insert = MasterTahun()
#         insert.tahun = tahun

#         insert.save()

#         return redirect('SPPD:tahun')

# def editTahun(request, idedit=""):
#     if request.method == "POST":
#         tahun = request.POST['thnEdit']

#         MasterTahun.objects.filter(id=idedit).update(tahun = tahun)

#         return redirect('SPPD:tahun')

# def hapusTahun(request, idedit):
#     hapus = MasterTahun.objects.get(id=idedit)

#     hapus.delete()
#     return redirect('SPPD:tahun')