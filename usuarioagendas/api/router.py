from rest_framework.routers import DefaultRouter
from usuarioagendas.api.view import UsuarioApiRegistroViewSet

router_usuario = DefaultRouter()
router_usuario = DefaultRouter()

router_usuario.register(
    prefix='usuario', basename='usuarios', viewset=UsuarioApiRegistroViewSet,

)

