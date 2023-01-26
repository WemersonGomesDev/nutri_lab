from django.contrib import admin
from .models import Pacientes, DadosPaciente,Opcao, Refeicao


admin.site.register(Pacientes)
admin.site.register(DadosPaciente)
admin.site.register(Opcao)
admin.site.register(Refeicao)