from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from ..decorators import *

# Create your views here.
@login_required
@is_verified()
@require_http_methods(["GET"])
def index(request):
    title = 'Dashboard'
    contex = {
        'title' : title
    }
    return render(request, 'dashboard/index.html', contex)