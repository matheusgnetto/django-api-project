from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.app.Funcionarios.views import FuncionarioViewSet
from api.app.Funcionarios.views import Funcionario_brlViewSet

route = routers.DefaultRouter()
route.register('funcionarios', FuncionarioViewSet, basename = 'Funcionarios')
route.register('funcionarios_brl', Funcionario_brlViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
