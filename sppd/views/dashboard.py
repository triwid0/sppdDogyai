from django.shortcuts import render, redirect
# from ..models import Task
# from ..forms import TaskForm

# Create your views here.
def index(request):
    title = 'Dashboard'
    contex = {
        'title' : title
    }
    return render(request, 'dashboard/index.html', contex)