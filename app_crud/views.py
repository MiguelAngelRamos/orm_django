from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from django.contrib import messages

class IndexCrudView(View):
    template_name = 'app_crud/index.html'

    def get(self, request):
        context = {
            'items': Item.objects.all(),
            'form': ItemForm(),
            "edit_form": ItemForm(auto_id='edit-%s'), # esto es para que los campos del formulario de edición tengan un id diferente al formulario de creación, lo cual es importante para evitar conflictos en el DOM y para poder seleccionar los elementos correctamente con JavaScript si es necesario.
        } # Es diccionario que podemos pasar al html para mostrar datos dinámicos
        return render(request, self.template_name, context)
    

    def post(self, request):
        # Realizar la obtencion de el proceso de crear, actalizar o eliminar un item
        # llamar a dicha accion por medio de metodos privados
        #* todo se hace con una condicional o bifuracion (primero debes dejar listas las herramientas 
        # * en los html para que la vista pueda capturar la accion que se desea realizar)
        action = request.POST.get('action') # el valor de la varialbe action es 'create' por que lo toma del value del input hidden del formulario del html
        

        actions_dic = {
            'create': self._handle_create,
            'update': self._handle_update,
            'delete': self._handle_delete,
        }

        handler = actions_dic.get(action) # handler va tener una referencia a la funcion que se encarga de crear un item, es decir, va ser igual a self._handle_create

        if handler:
            return handler(request) # _handle_create(request), _handle_update(request)
        else:
            messages.error(request, 'Acción no válida.')
        return redirect('index_crud') # si no se encuentra la accion, redirige a la misma pagina (GET)

    def _handle_create(self, request):
        
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item creado exitosamente')
        else:
            messages.error(request, 'Error al crear el item. Por favor, corrige los errores en el formulario.')
        return redirect('index_crud')
    

        #  if not form.is_valid():
        #     messages.error(request, 'Error al crear el item. Por favor, corrige los errores en el formulario.')
        #     return redirect('index_crud')
        # form.save()
        # messages.success(request, 'Item creado exitosamente.')
        # return redirect('index_crud')

    def _handle_update(self, request):
        # Antes de realizar una actualizacion lo que debemos es identificar el item que deseamos actualizar y esto lo haremos
        # Mediante el id del item
        # Ejemplo User.objects.filter(id=1).update(active=True)

        item = get_object_or_404(Item, id=request.POST.get('item_id')) # obtenemos el item a actualizar, si no se encuentra el item con el id proporcionado, se lanzará una excepción Http404 que resultará en una página de error 404 para el usuario.
        form = ItemForm(request.POST, instance=item) # el argumento instance=item le indica a Django que queremos actualizar ese item en lugar de crear uno nuevo. Si el formulario es válido, al llamar a form.save() se actualizará el registro existente en la base de datos en lugar de crear uno nuevo.
        if form.is_valid():
            form.save()
            messages.success(request, 'Item actualizado exitosamente.')
        return redirect('index_crud')
    
    def _handle_delete(self, request):
        item = get_object_or_404(Item, id=request.POST.get('item_id')) # obtenemos el item a eliminar, si no se encuentra el item con el id proporcionado, se lanzará una excepción Http404 que resultará en una página de error 404 para el usuario.
        nombre = item.nombre
        item.delete() # eliminamos el item de la base de datos
        messages.success(request, f'Item "{nombre}" eliminado exitosamente.')
        return redirect('index_crud')