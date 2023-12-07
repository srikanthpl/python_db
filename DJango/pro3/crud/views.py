# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import YourModel
from .forms import YourModelForm

def index(request):
    items = YourModel.objects.all()
    return render(request, 'index.html', {'items': items})

def create(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = YourModelForm()
    return render(request, 'create.html', {'form': form})

def update(request, pk):
    item = get_object_or_404(YourModel, pk=pk)
    if request.method == 'POST':
        form = YourModelForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = YourModelForm(instance=item)
    return render(request, 'update.html', {'form': form})

def delete(request, pk):
    item = get_object_or_404(YourModel, pk=pk)
    item.delete()
    return redirect('index')