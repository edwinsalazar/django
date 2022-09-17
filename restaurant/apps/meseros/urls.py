from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('meseros/', views.meseros, name='meseros'),
    path('meseros/crear', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('meseros/editar/<int:id>', views.editar, name='editar'),

    # Urls para vistas basadas en clases
    path('meseros_list_vc/', views.MeserosList.as_view(), name='meseros_list_vc'),
    path('meseros_create_vc/', views.MeserosCreate.as_view(), name='meseros_create_vc'),
    path('meseros_edit_vc/<int:pk>', views.MeserosUpdate.as_view(), name='meseros_edit_vc'),
    path('meseros_delete_vc/<int:pk>', views.MeserosDelete.as_view(), name='meseros_delete_vc'),
    path('meseros_delete_vc/<int:pk>', views.MeserosDelete.as_view(), name='meseros_delete_vc'),

    # Urls Serializador con Django
    path('meseros_list_serializer/', views.listMeserosSerializer, name='meseros_list_serializer'),

    # Urls Serializador con Rest_Framework
    path('meseros_list_drf/', views.MeserosApiView.as_view(), name='meseros_list_drf'),
    path('meseros_api_view/', views.meseros_api_view, name='meseros_api_view'),
    path('meseros_detail_view/<int:pk>', views.meseros_detail_view, name='meseros_detail_view'),

]
