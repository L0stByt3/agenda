from usuarioagendas.models import UsuarioSistema
from agenda.models import Telefonos
from agenda.api.serializer import AgendaRegistroSerializer, TelefonoRegistroSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

class AgendaApiRegistroViewSet(ModelViewSet):
    model = UsuarioSistema
    permission_classes = [AllowAny]
    serializer_class = AgendaRegistroSerializer
    queryset = UsuarioSistema.objects.all()

class TelefonoRegistroApiViewSet(ModelViewSet):
    model = Telefonos
    permission_classes = [IsAuthenticated]
    serializer_class = TelefonoRegistroSerializer
    queryset = Telefonos.objects.all()
