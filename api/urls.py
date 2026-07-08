from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/<str:id>/', views.detalle_producto, name='detalle_producto'),
    path('productos/actualizar/<str:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/eliminar/<str:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('ventas/', views.listar_ventas, name='listar_ventas'), 
]
