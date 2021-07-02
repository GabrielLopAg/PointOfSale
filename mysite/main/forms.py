from django import forms
from django.forms import *
from main.models import *


class ProductsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Productos
        fields = '__all__'
        widgets = {
            'sku': NumberInput(
                attrs={
                    'placeholder': 'Ingrese el codigo de referencia',
                }
            ),
            'nombre_prod': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del producto',
                }
            ),
            'categoria': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la categoria',
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Ingrese una descipción',
                    'rows': 2,
                    'cols': 50
                }
            ),
            'cotizacion': NumberInput(
                attrs={
                    'placeholder': 'Ingrese la cotización',
                }
            ),
            'precio_de_venta': NumberInput(
                attrs={
                    'placeholder': 'Ingrese el precio de venta',
                }
            ),
            'costo_unitario': NumberInput(
                attrs={
                    'placeholder': 'Ingrese el costo unitario',
                }
            ),
            'costo_paquete': NumberInput(
                attrs={
                    'placeholder': 'Ingrese el costo por paquete',
                }
            ),
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):  #         
    #     cleaned = super().clean()
    #     if cleaned['Sku'] == '22':
    #         self.add_error('Sku', 'Ya existe')
    #     print(cleaned)
    #     return cleaned


class ProvidersForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Proveedores
        fields = '__all__'
        widgets = {
            'nombre_comercial': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la empresa',
                }
            ),
            'nombre_representante': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del representante',
                }
            ),
            'tel_movil': TextInput(
                attrs={
                    'placeholder': 'Ingrese el telefono movil',
                }
            ),
            'tel_fijo': TextInput(
                attrs={
                    'placeholder': 'Ingrese el telefono fijo',
                    'rows': 2,
                    'cols': 50
                }
            ),
            'correo': TextInput(
                attrs={
                    'placeholder': 'Ingrese un correo',
                }
            ),
            'municipio': TextInput(
                attrs={
                    'placeholder': 'Ingrese el municipio',
                }
            ),
            'colonia': TextInput(
                attrs={
                    'placeholder': 'Ingrese la colonia',
                }
            ),
            'calle': TextInput(
                attrs={
                    'placeholder': 'Ingrese la calle',
                }
            ),
            'pagina_web': TextInput(
                attrs={
                    'placeholder': 'Ingrese la pagina web',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class SalesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Ventas
        fields = '__all__'
        widgets = {
            'municipio': TextInput(
                attrs={
                    'placeholder': 'Ingrese el municipio',
                }
            ),
            'colonia': TextInput(
                attrs={
                    'placeholder': 'Ingrese la colonia',
                }
            ),
            'calle': TextInput(
                attrs={
                    'placeholder': 'Ingrese la calle',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ExpensesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Gastos
        fields = '__all__'

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class StoreForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Almacenes
        fields = '__all__'

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data