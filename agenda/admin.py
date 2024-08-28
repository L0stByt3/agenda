from django.contrib import admin

from agenda.models import Telefonos

@admin.register(Telefonos)
class TelefonosAdmin(admin.ModelAdmin):
   list_display = ['id','numero','usuarioagenda']
