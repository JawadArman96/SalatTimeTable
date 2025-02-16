from django.urls import path
from . import views

urlpatterns = [
    # Example route for the home page
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list')
]
