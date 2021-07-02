from main.models2 import BaseModel
from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from itertools import chain
from datetime import datetime
from crum import get_current_user


class Productos(BaseModel):
    sku = models.BigIntegerField(unique='True', verbose_name='Sku')
    nombre_prod = models.CharField(max_length=25, verbose_name='Producto')
    categoria = models.CharField(max_length=25, verbose_name='Categoria')
    descripcion = models.TextField(verbose_name='Descripción')
    cotizacion = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Cotización')
    precio_de_venta = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Precio de venta')
    costo_unitario = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Costo unitario')
    costo_paquete = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Costo por paquete')

    def __str__(self):
        return self.nombre_prod

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Productos, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Ventas(models.Model):
    # num_venta = models.AutoField(primary_key='True', verbose_name='Número de venta')
    municipio = models.CharField(max_length=30, verbose_name='Municipio')
    colonia = models.CharField(max_length=30, verbose_name='Colonia')
    calle = models.CharField(max_length=50, verbose_name='Calle')
    fecha_de_venta = models.DateTimeField(auto_now_add='True', verbose_name='Fecha de venta')
    STATUS = (
        ('Vendido', 'Vendido'),
        ('Pendiente', 'Pendiente'),
    )
    estado_de_venta = models.CharField(max_length=25, choices=STATUS, verbose_name='Estado de venta')
    monto_total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Monto total')
    productos = models.ManyToManyField(Productos)    

    def toJSON(self):
        item = model_to_dict(self, exclude=['productos'])     
        item['fecha_de_venta'] = self.fecha_de_venta.strftime('%Y-%m-%d a las %H:%M')  
        return item
    
    class Meta:
        db_table = 'ventas'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class Proveedores(models.Model):
    # id_proveedor = models.AutoField(primary_key='True', verbose_name='ID del proveedor')
    nombre_comercial = models.CharField(max_length=30, verbose_name='Nombre comercial')
    nombre_representante = models.CharField(max_length=30, verbose_name='Nombre del representante')
    tel_movil = models.CharField(max_length=20, verbose_name='Telefono movil')
    tel_fijo = models.CharField(max_length=20, verbose_name='Telefono fijo')
    correo = models.EmailField(verbose_name='Correo')
    municipio = models.CharField(max_length=30, verbose_name='Municipio')
    colonia = models.CharField(max_length=30, verbose_name='Colonia')
    calle = models.CharField(max_length=50, verbose_name='Calle')
    pagina_web = models.CharField(max_length=200, verbose_name='Pagina web')
    productos = models.ManyToManyField(Productos)

    def __str__(self):
        return self.nombre_comercial

    def toJSON(self):  # este metodo convierte el modelo en diccionario
        item = model_to_dict(self, exclude=['productos'])
        return item

    class Meta:
        db_table = 'proveedores'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']


class Almacenes(models.Model):
    municipio = models.CharField(max_length=30, verbose_name='Municipio')
    colonia = models.CharField(max_length=30, verbose_name='Colonia')
    calle = models.CharField(max_length=50, verbose_name='Calle')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    productos = models.ManyToManyField(Productos)

    def toJSON(self):
        item = model_to_dict(self, exclude=['productos'])        
        return item

    class Meta:
        db_table = 'almacenes'
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'
        ordering = ['id']


class Sucursales(models.Model):
    # cambiar de 'id_sucursal' a 'sucursal'
    sucursal = models.OneToOneField(Almacenes, on_delete=models.CASCADE, primary_key=True, verbose_name='Sucursal')
    telefono = models.CharField(max_length=20, verbose_name='Telefono fijo')

    class Meta:
        db_table = 'sucursales'
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
        ordering = ['sucursal']


class Gastos(models.Model):
    agua = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Agua')
    renta = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Renta')
    luz = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Luz')
    internet = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Internet')
    fecha_pago = models.DateField(auto_now='True', verbose_name='Fecha de pago')
    sucursal = models.ForeignKey(Sucursales, on_delete=models.CASCADE)

    def toJSON(self):
        item = model_to_dict(self, exclude=['sucursal'])        
        item['fecha_pago'] = self.fecha_pago.strftime('%Y-%m-%d') 
        # item['sucursal'] = self.sucursal.toJSON()
        return item

    class Meta:
        db_table = 'gastos'
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        ordering = ['id']