from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:pk_id>/', views.product_detail, name="product_detail"),
    path('add/', views.add_product, name="add_product"),
    path('update/<str:pk_id>/', views.update_product, name="update_product"),
    path('delete/<str:pk_id>/', views.delete_product, name="delete_product"),
]
