from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from usuarioagendas.models import UsuarioSistema
from usuarioagendas.api.serializer import UsuarioAgendaSerializer
from agenda.models import  Telefonos

class TelefonoRegistroSerializer(ModelSerializer):
    usuarioagenda = serializers.PrimaryKeyRelatedField(queryset=UsuarioSistema.objects.all())
    class Meta:
        model = Telefonos
        fields = ['numero','usuarioagenda']


class AgendaRegistroSerializer(ModelSerializer):
    telefonos_data = TelefonoRegistroSerializer(source='numeros', many=True, read_only=True)

    class Meta:
        model = UsuarioSistema
        fields = ['usuario', 'telefono','telefonos_data']

    def validate_telefonos_data(self, value):
        numeros = [telefono['numero'] for telefono in value]
        if len(numeros) != len(set(numeros)):
            raise serializers.ValidationError("Los números de teléfono no pueden repetirse.")
        return value