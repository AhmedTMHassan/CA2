from django.urls import path
from .views import ProductListView, ProductDetailView, MakeListView

app_name = 'shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='prod_list'),  # List of all products
    path('product/<uuid:pk>/',ProductDetailView.as_view(), name='prod_detail'),
    path('make/', MakeListView.as_view(), name='make_list'),  # List of all makes
    path('make/<str:make_name>/', ProductListView.as_view(), name='prod_list_by_make'), 
]
