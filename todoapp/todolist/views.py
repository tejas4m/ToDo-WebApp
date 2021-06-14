from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')  

    context = { 'tasks' : tasks, 'form' : form}
    return render(request , 'todolist/list.html' , context )