from django.urls.base import reverse_lazy
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from main.models import Ventas
from main.forms import SalesForm


class SalesListView(ListView):
    model = Ventas
    template_name = 'sales/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # data = Ventas.objects.get(sku=request.POST['id']).toJSON()
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Ventas.objects.all():
                    data.append(i.toJSON())  # coleccion de diccionarios
                else:
                    pass
                    # data["error"] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ventas'
        context['create_url'] = reverse_lazy('main:sales_create')
        context['list_url'] = reverse_lazy('main:sales_list')
        context['entity'] = 'Ventas'
        return context


class SalesCreateView(CreateView):
    model = Ventas
    form_class = SalesForm
    template_name = 'sales/create.html'
    success_url = reverse_lazy('main:sales_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = SalesForm(request.POST)
                data = form.save()  # metodo save sobreescrito en SalesForm
            else:
                data['error'] = 'No ha ingresado a ninguna opción.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir venta'
        context['list_url'] = reverse_lazy('main:sales_list')
        context['entity'] = 'Venta'
        context['action'] = 'add'
        return context


class SalesUpdateView(UpdateView):
    model = Ventas
    form_class = SalesForm
    template_name = 'sales/create.html'
    success_url = reverse_lazy('main:sales_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar venta'
        context['list_url'] = reverse_lazy('main:sales_list')
        context['entity'] = 'Venta'
        context['action'] = 'edit'
        return context


class SalesDeleteView(DeleteView):
    model = Ventas
    form_class = SalesForm
    template_name = 'sales/delete.html'
    success_url = reverse_lazy('main:sales_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar venta'
        context['list_url'] = reverse_lazy('main:sales_list')
        context['entity'] = 'Venta'
        return context