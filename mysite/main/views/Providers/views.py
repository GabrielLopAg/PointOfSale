from django.http import JsonResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from main.models import Proveedores
from main.forms import ProvidersForm

class ProvidersListView(ListView):
    model = Proveedores
    template_name = 'providers/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # data = Proveedores.objects.get(sku=request.POST['id']).toJSON()
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Proveedores.objects.all():
                    data.append(i.toJSON())  # coleccion de diccionarios
                else:
                    pass
                    # data["error"] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)  # para serializar los objetos safe=False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proveedores'
        context['create_url'] = reverse_lazy('main:providers_create')
        context['list_url'] = reverse_lazy('main:providers_list')
        context['entity'] = 'Proveedores'
        return context


class ProvidersCreateView(CreateView):
    model = Proveedores
    form_class = ProvidersForm
    template_name = 'providers/create.html'
    success_url = reverse_lazy('main:providers_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = ProvidersForm(request.POST)
                data = form.save()  # metodo save sobreescrito en ProductsForm
            else:
                data['error'] = 'No ha ingresado a ninguna opción.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir proveedor'
        context['list_url'] = reverse_lazy('main:providers_list')
        context['entity'] = 'Proveedor'
        context['action'] = 'add'
        return context


class ProvidersUpdateView(UpdateView):
    model = Proveedores
    form_class = ProvidersForm
    template_name = 'providers/create.html'
    success_url = reverse_lazy('main:providers_list')

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
        context['title'] = 'Actualizar proveedor'
        context['list_url'] = reverse_lazy('main:providers_list')
        context['entity'] = 'Proveedor'
        context['action'] = 'edit'
        return context


class ProvidersDeleteView(DeleteView):
    model = Proveedores
    form_class = ProvidersForm
    template_name = 'providers/delete.html'
    success_url = reverse_lazy('main:providers_list')

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
        context['title'] = 'Borrar proveedor'
        context['list_url'] = reverse_lazy('main:providers_list')
        context['entity'] = 'Proveedor'
        return context