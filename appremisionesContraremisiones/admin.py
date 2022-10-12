from django.contrib import admin

# Register your models here.
from .models import Parentesco, Acompanante, TipoIdentificacion, Remision_Contraremision, Profesional, Afiliado, Servicio_Remitido


# Register your models here.

class AcompananteAdmin(admin.ModelAdmin):
    list_display = ["tipoIdentificacion", "numIdentificacion", "nombreP", "nombreS",
                    "apellidoP", "apellidoS"]


admin.site.register(Parentesco)
admin.site.register(Acompanante, AcompananteAdmin)
admin.site.register(TipoIdentificacion)
admin.site.register(Remision_Contraremision)
admin.site.register(Profesional)
admin.site.register(Servicio_Remitido)
admin.site.register(Afiliado)