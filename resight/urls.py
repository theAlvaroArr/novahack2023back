from django.urls import path

from .views import ListarGafas, CrearGafa

urlpatterns = [
    path("listar/", ListarGafas.as_view(), name="listar"),
    path("crear/", CrearGafa.as_view(), name="crear")
]
