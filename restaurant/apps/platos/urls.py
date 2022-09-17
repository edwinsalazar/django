from django.urls import path
from . import views


urlpatterns = [

    path('platos/', views.PlatosList.as_view(), name='platos_list_vc'),
    path('platos/buscar/', views.platos_search, name='platos_search'),

    # Urls Serializador con Django
    path('platos_list_serializer/', views.listPlatosSerializer, name='listPatos_serializer'),

    # Urls Serializador con DjangoRestFramework
    path('platos_list_drf/', views.plato_api_view, name='platos_list_drf'),
    path('platos_detail_id/<int:pk>', views.plato_detail_id, name='platos_detail_id'),
    path('platos_update_view/<int:pk>', views.plato_update_view, name='platos_update_view'),
    path('platos_delete_view/<int:pk>', views.platos_delete_view, name='platos_delete_view'),
]
