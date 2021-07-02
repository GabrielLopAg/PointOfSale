from main.views.Products.views import *
from main.views.Providers.views import *
from main.views.Sales.views import *
from main.views.Expenses.views import *
from main.views.Store.views import *
from main.views.Dashboard.views import *
from main.views.Vistas.views import *
from django.urls import path

app_name = 'main'

urlpatterns = [
    # productos
    path("products/list/", ProductsListView.as_view(), name="products_list"),
    path("products/add/", ProductsCreateView.as_view(), name="products_create"),
    path("products/update/<int:pk>/", ProductsUpdateView.as_view(), name="products_update"),
    path("products/delete/<int:pk>/", ProductsDeleteView.as_view(), name="products_delete"),
    path("products/form/", ProductsFormView.as_view(), name="products_form"),
    # proveedores
    path("providers/list/", ProvidersListView.as_view(), name="providers_list"),
    path("providers/add/", ProvidersCreateView.as_view(), name="providers_create"),
    path("providers/update/<int:pk>/", ProvidersUpdateView.as_view(), name="providers_update"),
    path("providers/delete/<int:pk>/", ProvidersDeleteView.as_view(), name="providers_delete"),
    # ventas
    path("sales/list/", SalesListView.as_view(), name="sales_list"),
    path("sales/add/", SalesCreateView.as_view(), name="sales_create"),
    path("sales/update/<int:pk>/", SalesUpdateView.as_view(), name="sales_update"),
    path("sales/delete/<int:pk>/", SalesDeleteView.as_view(), name="sales_delete"),
    # gastos
    path("expenses/list/", ExpensesListView.as_view(), name="expenses_list"),
    path("expenses/add/", ExpensesCreateView.as_view(), name="expenses_create"),
    path("expenses/update/<int:pk>/", ExpensesUpdateView.as_view(), name="sexpenses_update"),
    path("expenses/delete/<int:pk>/", ExpensesDeleteView.as_view(), name="expenses_delete"),
    # almacenes
    path("store/list/", StoreListView.as_view(), name="store_list"),
    path("store/add/", StoreCreateView.as_view(), name="store_create"),
    path("store/update/<int:pk>/", StoreUpdateView.as_view(), name="store_update"),
    path("store/delete/<int:pk>/", StoreDeleteView.as_view(), name="store_delete"),
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # vistas
    path('prod_prov/', Prod_ProvView, name='prod_prov'),
    path('prod_sales/', Prod_SalesView, name='prod_sales'),
    path('prod_store/', Prod_StoreView, name='prod_store'),
]
