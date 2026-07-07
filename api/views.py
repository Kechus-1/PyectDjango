from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


productos = [
    {"id": 1, "nombre": "Laptop", "precio": 12500, "stock": 5},
    {"id": 2, "nombre": "Mouse", "precio": 250, "stock": 20},
    {"id": 3, "nombre": "Teclado", "precio": 600, "stock": 10},
]


def inicio(request):
    return JsonResponse({
        "mensaje": "API de ventas funcionando",
        "rutas": [
            "/api/productos/",
            "/api/productos/1/"
        ]
    })


def listar_productos(request):
    return JsonResponse({
        "productos": productos
    })


def detalle_producto(request, id):
    for producto in productos:
        if producto["id"] == id:
            return JsonResponse(producto)

    return JsonResponse({
        "error": "Producto no encontrado"
    }, status=404)

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

        nuevo_producto = {
            "id": len(productos) + 1,
            "nombre": datos["nombre"],
            "precio": datos["precio"],
            "stock": datos["stock"]
        }

        productos.append(nuevo_producto)

        return JsonResponse({
            "mensaje": "Producto creado correctamente",
            "producto": nuevo_producto
        }, status=201)

    return JsonResponse({
        "error": "Método no permitido"
    }, status=405)

@csrf_exempt
def actualizar_producto(request, id):
    if request.method == "PUT":
        datos = json.loads(request.body)

        for producto in productos:
            if producto["id"] == id:
                producto["nombre"] = datos.get("nombre", producto["nombre"])
                producto["precio"] = datos.get("precio", producto["precio"])
                producto["stock"] = datos.get("stock", producto["stock"])

                return JsonResponse({
                    "mensaje": "Producto actualizado correctamente",
                    "producto": producto
                })

        return JsonResponse({"error": "Producto no encontrado"}, status=404)

    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar_producto(request, id):
    if request.method == "DELETE":
        for producto in productos:
            if producto["id"] == id:
                productos.remove(producto)

                return JsonResponse({
                    "mensaje": "Producto eliminado correctamente",
                    "producto": producto
                })

        return JsonResponse({"error": "Producto no encontrado"}, status=404)

    return JsonResponse({"error": "Método no permitido"}, status=405)