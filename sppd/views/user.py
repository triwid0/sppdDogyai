from django.shortcuts import render, redirect
# from ..models import Task
# from ..forms import TaskForm

# Create your views here.
def index(request):
    title = 'MasterTahun'
    contex = {
        'title' : title
    }
    return render(request, 'user/index.html', contex)