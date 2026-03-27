from django.urls import path
from .views import IndexCrudView

urlpatterns = [
    path('', IndexCrudView.as_view(), name='index_crud'),
]