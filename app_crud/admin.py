from django.contrib import admin
from .models import Item
@admin.register(Item) # registra el modelo Item en el panel de administración de Django utilizando el decorador @admin.register para asociar la clase ItemAdmin con el modelo Item
class ItemAdmin(admin.ModelAdmin):
    #* Campos que se mostrarán como columnas en la lista del panel de administración para el modelo Item.
    list_display = ('id', 'nombre', 'precio', 'fecha_creacion') 
    #* Campos por los que se podrá filtrar en el panel de administración para el modelo Item.
    list_filter = ('fecha_creacion',) 
    #* Campos por los que se podrá buscar en el panel de administración para el modelo Item.
    search_fields = ('nombre', 'descripcion') 
    #* Ordenamiento por defecto en el panel de administración para el modelo Item (los más recientes primero).
    ordering = ('-fecha_creacion',) 
  