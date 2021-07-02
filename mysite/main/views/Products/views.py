from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.decorators import login_required

from main.models import Productos
from main.forms import ProductsForm


class ProductsListView(ListView):
    model = Productos
    template_name = 'products/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # data = Productos.objects.get(sku=request.POST['id']).toJSON()
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Productos.objects.all():  # Productos.objects.all() obtengo los datos de mi BD
                    data.append(i.toJSON())  # coleccion de diccionarios
                else:
                    pass
                    # data["error"] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)  # para serializar los objetos safe=False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('main:products_create')
        context['list_url'] = reverse_lazy('main:products_list')
        context['entity'] = 'Productos'
        return context


class ProductsCreateView(CreateView):
    model = Productos
    form_class = ProductsForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('main:products_list')
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = ProductsForm(request.POST)
                data = form.save()  # metodo save sobreescrito en ProductsForm
            else:
                data['error'] = 'No ha ingresado a ninguna opción.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # def post(self, request, *args, **kwargs):  # ejemplo del proceso de un post
    #     form = ProductsForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir producto'
        context['list_url'] = reverse_lazy('main:products_list')
        context['entity'] = 'Producto'
        context['action'] = 'add'
        return context


class ProductsUpdateView(UpdateView):
    model = Productos
    form_class = ProductsForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('main:products_list')

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
        context['title'] = 'Actualizar producto'
        context['list_url'] = reverse_lazy('main:products_list')
        context['entity'] = 'Producto'
        context['action'] = 'edit'
        return context


class ProductsDeleteView(DeleteView):
    model = Productos
    form_class = ProductsForm
    template_name = 'products/delete.html'
    success_url = reverse_lazy('main:products_list')

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
        context['title'] = 'Borrar producto'
        context['list_url'] = reverse_lazy('main:products_list')
        context['entity'] = 'Producto'
        return context


class ProductsFormView(FormView):  # esta clase verifica si mi formulario es valido
    form_class = ProductsForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('main:products_list')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Producto'
        context['list_url'] = reverse_lazy('main:products_list')
        context['entity'] = 'Producto'
        context['action'] = 'add'
        return context


