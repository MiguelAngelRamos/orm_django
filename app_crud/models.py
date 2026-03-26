from django.db import models

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2) # varchar(10,2) en SQL
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_index=True) # se traduce en sql a timestamp con valor por defecto CURRENT_TIMESTAMP y un índice para optimizar consultas por fecha de creación

    # La clase Meta se utiliza para configurar opciones adicionales del modelo, como el nombre de la tabla en la base de datos, el ordenamiento por defecto, etc. en el panel de administración de Django.
    #* La clase Meta no afecta a estructura de la tabla que se creara con este modelo, solo a su comportamiento en el panel de administración y otras funcionalidades de Django.
    class Meta: 
        ordering = ['-fecha_creacion'] # ordena los items por fecha de creación de forma descendente (los más recientes primero)
        verbose_name = 'Item' # nombre singular del modelo para mostrar en el panel de administración
        verbose_name_plural = 'Items' # nombre plural del modelo para mostrar en el panel de administración

    def __str__(self):
        return f'{self.nombre} (${self.precio})' # esto hace que al imprimir un objeto de tipo Item se muestre su nombre y precio en lugar de la dirección de memoria