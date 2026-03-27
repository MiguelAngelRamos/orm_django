from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .models import Item
from .forms import ItemForm
from django.contrib import messages

class IndexCrudView(View):
    template_name = 'app_crud/index.html'

    def get(self, request):
        context = {
            'items': Item.objects.all(),
            'form': ItemForm(),
        } # Es diccionario que podemos pasar al html para mostrar datos dinámicos
        return render(request, self.template_name, context)
    

    def post(self, request):
        # Realizar la obtencion de el proceso de crear, actalizar o eliminar un item
        # llamar a dicha accion por medio de metodos privados
        #* todo se hace con una condicional o bifuracion (primero debes dejar listas las herramientas 
        # * en los html para que la vista pueda capturar la accion que se desea realizar)
        action = request.POST.get('action') # el valor de la varialbe action es 'create' por que lo toma del value del input hidden del formulario del html

        actions = {
            'create': self._handle_create,
        }

        handler = actions.get(action) # handler va tener una referencia a la funcion que se encarga de crear un item, es decir, va ser igual a self._handle_create

        if handler:
            return handler(request) # _handle_create(request)
        return redirect('index_crud') # si no se encuentra la accion, redirige a la misma pagina (GET)

    def _handle_create(self, request):
        print("Llegaste a la funcion de crear un item")
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item creado exitosamente')
        else:
            messages.error(request, 'Error al crear el item. Por favor, corrige los errores en el formulario.')