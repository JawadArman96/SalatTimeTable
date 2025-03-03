from django.urls import path
from . import views

urlpatterns = [
    # Example route for the home page
    # path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.login_view, name='login_view'),
    path('login/', views.login_view, name='login_view'),
    path("logout/", views.logout_view, name="logout"),
    path('prayertime/', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
]
