from django.shortcuts import render
from main.models import *


def Prod_ProvView(response):
    data = {
        'title': 'Consulta Proveedores',
        'provs': Proveedores.objects.all().values('productos__sku', 'productos__nombre_prod', 'nombre_comercial', 'correo', 'pagina_web'),
        'entity': 'Reporte'
    }    
    return render(response, 'vistas/prod_prov.html', data)


def Prod_SalesView(response):
    data = {
        'title': 'Consulta Ventas',
        'sales': Ventas.objects.all().values('id', 'productos__nombre_prod', 'productos__categoria', 'productos__precio_de_venta', 'estado_de_venta', 'monto_total'),        
        'entity': 'Reporte'
    }    
    return render(response, 'vistas/prod_sales.html', data)


def Prod_StoreView(response):
    data = {
        'title': 'Consulta Stock',
        'store': Almacenes.objects.all().values('productos__sku', 'productos__nombre_prod', 'productos__categoria', 'id', 'cantidad'),      
        'entity': 'Reporte'
    }    
    return render(response, 'vistas/prod_store.html', data)


def Expenses_StoreView(response):
    data = {
        'title': 'Consulta Gastos',
        'store': Almacenes.objects.all().values('almacen__id', 'almacen__municipio', 'id', 'agua', 'luz'),      
        'entity': 'Reporte'
    }    
    return render(response, 'vistas/expenses_store.html', data)