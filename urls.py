from django.contrib import admin
from django.urls import path
from views import (
    login_view,
    dashboard_view,
    clientes_view,
    financeiro_view,
    materiais_view,
    logout_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),                 # Página inicial = login
    path('dashboard/', dashboard_view, name='dashboard'),
    path('clientes/', clientes_view, name='clientes'),
    path('financeiro/', financeiro_view, name='financeiro'),
    path('materiais/', materiais_view, name='materiais'),
    path('logout/', logout_view, name='logout'),
]
