from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.

def index(request):
    items = Inventory.objects.all()
    # return render(request, 'index.html')
    context = {
        'items': items,
    }

    return render(request, 'index.html', context)


def add_inventory(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = InventoryForm()
        return render(request, 'add_new.html', {'form': form})


def update_inventory(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = InventoryForm(instance=item)
        return render(request, 'update_inventory.html', {"form": form})


def delete_inventory(request, pk):
    Inventory.objects.filter(id=pk).delete()
    items = Inventory.objects.all()

    return render(request, 'index.html', {"items": items})