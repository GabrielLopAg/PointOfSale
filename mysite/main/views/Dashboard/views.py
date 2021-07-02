from django.db.models.aggregates import Sum
from django.db.models import Sum
from django.db.models.fields import DecimalField, FloatField
from main.models import Ventas
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Coalesce
from datetime import datetime


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_graph_sales_months(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):        
                total = Ventas.objects.filter(fecha_de_venta__year=year, fecha_de_venta__month=m).aggregate(r=Coalesce(Sum('monto_total', output_field=FloatField()), 0.00)).get('r')
                data.append(total)
        except Exception as e:            
            print(e)        
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Panel de administrador'
        context['graph_sales_months'] = self.get_graph_sales_months()
        return context
