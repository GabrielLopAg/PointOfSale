from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.decorators import login_required

from main.models import Almacenes
from main.forms import StoreForm


class StoreListView(ListView):
    model = Almacenes
    template_name = 'store/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # data = Almacenes.objects.get(sku=request.POST['id']).toJSON()
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Almacenes.objects.all():  # Almacenes.objects.all() obtengo los datos de mi BD
                    data.append(i.toJSON())  # coleccion de diccionarios
                else:
                    pass
                    # data["error"] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)  # para serializar los objetos safe=False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Almacenes'
        context['create_url'] = reverse_lazy('main:store_create')
        context['list_url'] = reverse_lazy('main:store_list')
        context['entity'] = 'Almacenes'
        return context


class StoreCreateView(CreateView):
    model = Almacenes
    form_class = StoreForm
    template_name = 'store/create.html'
    success_url = reverse_lazy('main:store_list')
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = StoreForm(request.POST)
                data = form.save()  # metodo save sobreescrito en storeForm
            else:
                data['error'] = 'No ha ingresado a ninguna opción.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # def post(self, request, *args, **kwargs):  # ejemplo del proceso de un post
    #     form = storeForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir Almacen'
        context['list_url'] = reverse_lazy('main:store_list')
        context['entity'] = 'Almacen'
        context['action'] = 'add'
        return context


class StoreUpdateView(UpdateView):
    model = Almacenes
    form_class = StoreForm
    template_name = 'store/create.html'
    success_url = reverse_lazy('main:store_list')

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
        context['title'] = 'Actualizar Almacen'
        context['list_url'] = reverse_lazy('main:store_list')
        context['entity'] = 'Almacen'
        context['action'] = 'edit'
        return context


class StoreDeleteView(DeleteView):
    model = Almacenes
    form_class = StoreForm
    template_name = 'store/delete.html'
    success_url = reverse_lazy('main:store_list')

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
        context['title'] = 'Borrar Almacen'
        context['list_url'] = reverse_lazy('main:store_list')
        context['entity'] = 'Almacen'
        return context


class StoreFormView(FormView):  # esta clase verifica si mi formulario es valido
    form_class = StoreForm
    template_name = 'store/create.html'
    success_url = reverse_lazy('main:store_list')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Almacen'
        context['list_url'] = reverse_lazy('main:store_list')
        context['entity'] = 'Almacen'
        context['action'] = 'add'
        return context


