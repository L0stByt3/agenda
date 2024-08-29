from rest_framework.serializers import ModelSerializer
from usuarioagendas.models import UsuarioSistema

class UsuarioAgendaSerializer(ModelSerializer):
    class Meta:
        model = UsuarioSistema
        fields = ['id','usuario', 'telefono']
