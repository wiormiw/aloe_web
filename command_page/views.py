from command_page.models import Command
from command_page.serializers import CommandSerializer
from rest_framework import viewsets

# Create your views here.
class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer