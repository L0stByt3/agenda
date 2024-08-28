from usuarioagendas.models import UsuarioSistema
from agenda.api.serializer import AgendaRegistroSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

class UsuarioApiRegistroViewSet(ModelViewSet):
    model = UsuarioSistema
    permission_classes = [AllowAny]
    serializer_class = AgendaRegistroSerializer
    queryset = UsuarioSistema.objects.all()