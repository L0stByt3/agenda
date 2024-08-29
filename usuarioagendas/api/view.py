from usuarioagendas.models import UsuarioSistema
from usuarioagendas.api.serializer import UsuarioAgendaSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

class UsuarioApiRegistroViewSet(ModelViewSet):
    model = UsuarioSistema
    permission_classes = [AllowAny]
    serializer_class = UsuarioAgendaSerializer
    queryset = UsuarioSistema.objects.all()