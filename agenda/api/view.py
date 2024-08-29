from usuarioagendas.models import UsuarioSistema
from agenda.models import Telefonos
from agenda.api.serializer import AgendaRegistroSerializer, TelefonoRegistroSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

class AgendaApiRegistroViewSet(ModelViewSet):
    model = Telefonos
    permission_classes = [AllowAny]
    serializer_class = AgendaRegistroSerializer
    queryset = UsuarioSistema.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        for usuario in queryset:
            telefonos_unicos = list({telefono.numero: telefono for telefono in usuario.numeros.all()}.values())
            usuario.numeros.set(telefonos_unicos, clear=True)
        return queryset

class TelefonoRegistroApiViewSet(ModelViewSet):
    model = Telefonos
    permission_classes = [AllowAny]
    serializer_class = TelefonoRegistroSerializer
    queryset = Telefonos.objects.all()
