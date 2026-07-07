from django.db import models

# Create your models here.
from mongoengine import Document, StringField, FloatField, IntField

class Producto(Document):
    nombre = StringField(required=True, max_length=150)
    precio = FloatField(required=True)
    stock = IntField(required=True)