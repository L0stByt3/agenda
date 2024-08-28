from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from usuarioagendas.models import UsuarioSistema
from usuarioagendas.api.serializer import UsuarioAgendaSerializer
from agenda.models import  Telefonos

class TelefonoRegistroSerializer(ModelSerializer):
    usuarioagenda = UsuarioAgendaSerializer()
    class Meta:
        model = Telefonos
        fields = ['numero','usuarioagenda']


class AgendaRegistroSerializer(ModelSerializer):
    telefonos_data = TelefonoRegistroSerializer(source='telefonos', many=True, read_only=True)

    class Meta:
        model = UsuarioSistema
        fields = ['usuario', 'telefono','telefonos_data']

