from rest_framework import viewsets
from .serializers import Taskserializers
from .models import Tasks


# Create your views here.
class TaskViewsets(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = Taskserializers