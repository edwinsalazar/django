from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/crear', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('clientes/editar/<int:id>', views.editar, name='editar'),

    # Urls para vistas basadas en clases
    path('cliente_list_vc/', views.ClienteList.as_view(), name='cliente_list_vc'),
    path('cliente_create_vc/', views.ClienteCreate.as_view(), name='cliente_create_vc'),
    path('cliente_edit_vc/<int:pk>', views.ClienteUpdate.as_view(), name='cliente_edit_vc'),
    path('cliente_delete_vc/<int:pk>', views.ClienteDelete.as_view(), name='cliente_delete_vc'),
    path('cliente_delete_vc/<int:pk>', views.ClienteDelete.as_view(), name='cliente_delete_vc'),

    # Urls Serializador con Django
    path('cliente_list_serializer/', views.listClienteSerializer, name='cliente_list_serializer'),

    # Urls Serializador con Rest_Framework
    path('cliente_list_drf/', views.ClienteApiView.as_view(), name='cliente_list_drf'),
    path('cliente_api_view/', views.cliente_api_view, name='cliente_api_view'),
    path('cliente_detail_view/<int:pk>', views.cliente_detail_view, name='cliente_detail_view'),

]
