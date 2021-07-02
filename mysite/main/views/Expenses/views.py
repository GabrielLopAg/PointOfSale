from django.http import JsonResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from main.models import Gastos
from main.forms import ExpensesForm

class ExpensesListView(ListView):
    model = Gastos
    template_name = 'expenses/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # data = Gastos.objects.get(sku=request.POST['id']).toJSON()
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Gastos.objects.all():
                    data.append(i.toJSON())  # coleccion de diccionarios
                else:
                    pass
                    # data["error"] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)  # para serializar los objetos safe=False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Gastos'
        context['create_url'] = reverse_lazy('main:expenses_create')
        context['list_url'] = reverse_lazy('main:expenses_list')
        context['entity'] = 'Gastos'
        return context


class ExpensesCreateView(CreateView):
    model = Gastos
    form_class = ExpensesForm
    template_name = 'expenses/create.html'
    success_url = reverse_lazy('main:expenses_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = ExpensesForm(request.POST)
                data = form.save()  # metodo save sobreescrito en ProductsForm
            else:
                data['error'] = 'No ha ingresado a ninguna opción.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir gasto'
        context['list_url'] = reverse_lazy('main:expenses_list')
        context['entity'] = 'Gasto'
        context['action'] = 'add'
        return context


class ExpensesUpdateView(UpdateView):
    model = Gastos
    form_class = ExpensesForm
    template_name = 'expenses/create.html'
    success_url = reverse_lazy('main:expenses_list')

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
        context['title'] = 'Actualizar gasto'
        context['list_url'] = reverse_lazy('main:expenses_list')
        context['entity'] = 'Gasto'
        context['action'] = 'edit'
        return context


class ExpensesDeleteView(DeleteView):
    model = Gastos
    form_class = ExpensesForm
    template_name = 'expenses/delete.html'
    success_url = reverse_lazy('main:expenses_list')

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
        context['title'] = 'Borrar gasto'
        context['list_url'] = reverse_lazy('main:expenses_list')
        context['entity'] = 'Gasto'
        return context