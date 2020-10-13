from django.urls import path
from . import views



app_name = 'venta'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('crear',views.NewView.as_view(), name=('crearVenta')),
    path('crearNuevaVenta/',views.crearNuevaVenta, name=('crearNuevaVenta')),
    path('modificar/<int:idVenta>',views.ModifyView.as_view(), name=('modificar')),
    path('modificar/venta/<int:idVenta>',views.modificarVenta, name=('modificarVenta')),
    path('eliminar/<int:idVenta>',views.eliminarVenta, name=('eliminar')),
]