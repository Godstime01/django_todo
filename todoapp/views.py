from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
  return render(request, 'index.html', {})

def dashboard(request):
  c_t = Todo.objects.all().count()
  f_t = Todo.objects.filter(status = True)
  cf_t = Todo.objects.filter(status = True).count()
  five_t = Todo.objects.all()[:5]
  if request.method == 'POST':
    todo = request.POST['todo']
    t = Todo.objects.create(todo = todo)
    t.save()
    
  return render(request, 'dashboard.html', {'todos':five_t, 'todo_count': c_t, 'comp_count': cf_t, 'comp': f_t})
  
def edit(request, pk):
  todo = Todo.objects.get(pk = pk)
  if request.method == 'POST':
    form = Edit(request.POST, instance = todo)
    
    if form.is_valid():
      form.save()
  else:
    form = Edit(instance = todo)
  return render(request, 'edit.html', {'form' : form})
  
def delete(request, pk):
  return render(request, 'delete.html')
  
