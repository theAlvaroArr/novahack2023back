from .models import Gafa
from django.http import HttpResponse
from .serializers import GafaSerializer
from rest_framework.generics import ListAPIView, CreateAPIView


def index(request):
    return HttpResponse("You're looking at question")


class ListarGafas(ListAPIView):
    queryset = Gafa.objects.all().filter(vendido=False)
    serializer_class = GafaSerializer


# post

class CrearGafa(CreateAPIView):
    queryset = Gafa.objects.all()
    serializer_class = GafaSerializer

    def perform_create(self, serializer):
        serializer.save(vendido=False)  # updated after creation
