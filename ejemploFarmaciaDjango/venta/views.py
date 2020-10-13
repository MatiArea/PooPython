from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse 
from django.views import generic
from datetime import datetime

from venta.models import Venta
from venta.forms import VentaForm

class IndexView(generic.ListView):
    template_name = 'venta/index.html'
    context_object_name = 'ventas'

    def get_queryset(self):
        return Venta.objects.all()
        

class NewView(generic.TemplateView):
    template_name = 'venta/crear.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['crearVenta'] = VentaForm()

        return context


class ModifyView(generic.TemplateView):
    model = Venta
    template_name = 'venta/modificar.html'
    
    def get_context_data(self,idVenta):
        context = super().get_context_data()
        venta = Venta.objects.get(id=idVenta) 
        horaFecha = venta.fechaHoraVenta

        context['venta'] = Venta.objects.get(id=idVenta)
        context['fecha'] = str(horaFecha.date())
        context['hora'] = str(horaFecha.time())
        
        return context



class DeleteView(generic.TemplateView):
    model = Venta
    template_name = 'venta/eliminar.html'

def crearNuevaVenta(request):
    nombre = request.POST.get('nombre')
    droga = request.POST.get('droga')
    obraSocial = request.POST.get('obraSocial')
    plan = request.POST.get('plan')
    importe = request.POST.get('importe')
    fecha = request.POST.get('fecha')
    hora = request.POST.get('hora')

    venta = Venta(nombreMedicamento=nombre,droga=droga,obraSocial=obraSocial,plan=plan,importe=importe,fechaHoraVenta=(fecha+' '+hora))
    venta.save()
    return redirect('/ventas/')


def modificarVenta(request,idVenta):
    try:
        venta = Venta.objects.get(id=idVenta)
        venta.nombreMedicamento = request.POST.get('nombre')
        venta.droga = request.POST.get('droga')
        venta.obraSocial = request.POST.get('obraSocial')
        venta.plan = request.POST.get('plan')
        venta.importe = request.POST.get('importe')
        venta.fechaHoraVenta = (request.POST.get('fecha'))+' '+(request.POST.get('hora'))
        venta.save()
        return redirect('/ventas/')
    except BaseException:
        return redirect('/ventas/')


def eliminarVenta(request,idVenta):
    try:
        venta = Venta.objects.get(id=idVenta)
        venta.delete()
        return redirect('/ventas/')
    except BaseException:
        return redirect('/ventas/')

