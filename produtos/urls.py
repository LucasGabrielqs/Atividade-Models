"""
URL configuration for produtos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from busca import views
from busca.views import ProdutosListView

urlpatterns = [
    path("", views.Index, name='index'),
    path("list/<str:choice>", views.Lista, name='listing'),
    path("detail/product/<int:pk>/", views.DetailProduct, name='detail-product'),
    path("create/product", views.create_product, name="create-product"),
    path("create/category", views.create_category, name="create-category"),
    path("create/supplier", views.create_supplier, name="create-supplier"),
    path("produtos/",ProdutosListView.as_view(),name="produto-list")
]
