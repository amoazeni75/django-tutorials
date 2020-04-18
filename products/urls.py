from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path("products/<int:pk>/", views.ProductDetailView.as_view(), name='product-detail'),
    path("api/products/", views.product_list, name='product-list-api'),
    path("api/products/<int:pk>/", views.product_detail, name='product-detail-api'),
    path("api/manufacturer/<int:pk>/", views.manufacturer_detail, name='manufacturer-detail-api'),
]
