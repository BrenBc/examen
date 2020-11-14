from django.db import models

class Categoria(models.Model):
    tipo_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_categoria

class Precio (models.Model):
    Precio = models.FloatField()
    tipo_precio = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_precio

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length= 50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.ForeignKey(Precio, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Fotografia(models.Model):
    fotografia = models.ImageField(blank=True,  )
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)

    def __str__(self):
        return self.fotografia.url


