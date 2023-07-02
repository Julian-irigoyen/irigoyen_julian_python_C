from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from .models import Productos
from .forms import ProductoForm

def index(request):

    return HttpResponse("Hola Mundo")

class Inicio(View):
    template_name= 'inicio.html'

    def post(self, request):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        
        return render(request, self.template_name, {'form': form})
    
    def get(self, request):
        productos = Productos.objects.all()
        form = ProductoForm()
        return render(request, self.template_name, {'form': form, 'productos': productos})
    
class Formulario(View):
    template_formulario= 'formulario.html'

    def post(self, request):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario')
        
        return render(request, self.template_formulario, {'form': form})
    
    def get(self, request):
        productos = Productos.objects.all()
        form = ProductoForm()
        return render(request, self.template_formulario, {'form': form, 'productos': productos})
