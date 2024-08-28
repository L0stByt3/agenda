from rest_framework.routers import DefaultRouter
from agenda.api.view import AgendaApiRegistroViewSet, TelefonoRegistroApiViewSet

router_agenda = DefaultRouter()
router_agenda = DefaultRouter()

router_agenda.register(
    prefix='agendas', basename='agendas', viewset=AgendaApiRegistroViewSet,

)

router_agenda.register(
    prefix='telefonos', basename='telefonos', viewset=TelefonoRegistroApiViewSet
)
