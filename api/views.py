from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Producto # Importamos tu nuevo modelo

def inicio(request):
    return JsonResponse({
        "mensaje": "API de ventas funcionando",
        "rutas": [
            "/api/productos/",
            "/api/productos/1/"
        ]
    })


def listar_productos(request):
    productos_db = Producto.objects.all()
    datos = [
        {"id": str(p.id), "nombre": p.nombre, "precio": p.precio, "stock": p.stock} 
        for p in productos_db
    ]
    return JsonResponse({"productos": datos})

def detalle_producto(request, id):
    try:
        producto = Producto.objects.get(id=id)
        return JsonResponse({
            "id": str(producto.id),
            "nombre": producto.nombre,
            "precio": producto.precio,
            "stock": producto.stock
        })
    except Producto.DoesNotExist:
        return JsonResponse({"error": "Producto no encontrado"}, status=404)

clientes = [
    {"id": 1, "nombre": "Juan Pérez", "correo": "juan@gmail.com"},
    {"id": 2, "nombre": "Ana López", "correo": "ana@gmail.com"},
]

ventas = [
    {"id": 1, "cliente_id": 1, "producto_id": 2, "cantidad": 3, "total": 750},
    {"id": 2, "cliente_id": 2, "producto_id": 1, "cantidad": 1, "total": 12500},
]


def listar_clientes(request):
    return JsonResponse({"clientes": clientes})


def listar_ventas(request):
    return JsonResponse({"ventas": ventas})

@csrf_exempt
def crear_producto(request):
    if request.method == "POST":
        datos = json.loads(request.body)
        nuevo_producto = Producto(
            nombre=datos["nombre"],
            precio=datos["precio"],
            stock=datos["stock"]
        )
        nuevo_producto.save() # Guarda en MongoDB
        return JsonResponse({
            "mensaje": "Producto guardado en base de datos",
            "producto": {"id": str(nuevo_producto.id), "nombre": nuevo_producto.nombre, "precio": nuevo_producto.precio, "stock": nuevo_producto.stock}
        }, status=201)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def actualizar_producto(request, id):
    if request.method == "PUT":
        datos = json.loads(request.body)
        try:
            producto = Producto.objects.get(id=id)
            producto.nombre = datos.get("nombre", producto.nombre)
            producto.precio = datos.get("precio", producto.precio)
            producto.stock = datos.get("stock", producto.stock)
            producto.save()
            return JsonResponse({"mensaje": "Producto actualizado", "producto": {"id": str(producto.id), "nombre": producto.nombre}})
        except Producto.DoesNotExist:
            return JsonResponse({"error": "Producto no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar_producto(request, id):
    if request.method == "DELETE":
        try:
            producto = Producto.objects.get(id=id)
            producto.delete() # Elimina de MongoDB
            return JsonResponse({"mensaje": "Producto eliminado de la base de datos"})
        except Producto.DoesNotExist:
            return JsonResponse({"error": "Producto no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)