from django.shortcuts import render
from django.views import View
from .models import Item
from .forms import ItemForm

class IndexCrudView(View):
    template_name = 'app_crud/index.html'

    def get(self, request):
        context = {
            'items': Item.objects.all(),
            'form': ItemForm(),
        } # Es diccionario que podemos pasar al html para mostrar datos dinámicos
        return render(request, self.template_name, context)
        