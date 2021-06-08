from django.shortcuts import render, redirect
from .models import Ferramenta
from .forms import FerramentaForm


def list_ferramentas(request):
    ferramentas = Ferramenta.objects.all()
    return render(request, 'ferramentas.html', {'ferramentas': ferramentas})


def create_ferramenta(request):
    form = FerramentaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_ferramentas')

    return render(request, 'ferramentas-form.html', {'form': form})


def update_ferramenta(request, id):
    ferramenta = Ferramenta.objects.get(id=id)
    form = FerramentaForm(request.POST or None, instance=ferramenta)

    if form.is_valid():
        form.save()
        return redirect('list_ferramentas')

    return render(request, 'ferramentas-form.html', {'form': form, 'ferramenta': ferramenta})


def delete_ferramenta(request, id):
    ferramenta = Ferramenta.objects.get(id=id)

    if request.method == 'POST':
        ferramenta.delete()
        return redirect('list_ferramentas')

    return render(request, 'ferr-delete-confirm.html', {'ferramenta': ferramenta})