from apps.platos.serializers import PlatosSerializer
from django.shortcuts import render


from .models import Platos

from django.views.generic import ListView
from django.db.models import Q
from django.core import serializers as ssr
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class PlatosList(ListView):
    model = Platos
    template_name = 'platos/platos_list_vc.html'


def platos_search(request):
    query = request.GET.get('q', '')
    #print("query: {}".format(query))
    results = (
        Q(nombre__icontains=query)
    )

    data_context = Platos.objects.filter(results).distinct()

    return render(request, 'platos/platos_search.html', context={'data': data_context, "query": query})

# Serializacion con Django


def listPlatosSerializer(request):
    list_platos = ssr.serialize('json', Platos.objects.all())
    return HttpResponse(list_platos, content_type='application/json')


@api_view(['GET', 'POST'])
def plato_api_view(request):
    if request.method == 'GET':
        queryset = Platos.objects.all()
        serializer_class = PlatosSerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PlatosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)


@api_view(['GET', 'PUT'])
def plato_update_view(request, pk):
    queryset = Platos.objects.filter(id=pk).first()
    if queryset:
        if request.method == 'GET':

            serializer_class = PlatosSerializer(queryset)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':

            serializer_class = PlatosSerializer(queryset, data=request.data)

            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_200_OK)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'No se encuentra el plato'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def platos_delete_view(request, pk):
    queryset = Platos.objects.filter(id=pk).first()
    if queryset:
        if request.method == 'GET':

            serializer_class = PlatosSerializer(queryset)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            #queryset = Cliente.objects.filter(id=pk).first()
            queryset.delete()
            return Response({'message': 'Pato eliminado correctamente'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se encuentra el plato'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def plato_detail_id(request, pk):
    queryset = Platos.objects.filter(id=pk).first()
    if queryset:
        if request.method == 'GET':

            serializer_class = PlatosSerializer(queryset)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
    return Response({'message': 'No se encuentra el plato'}, status=status.HTTP_400_BAD_REQUEST)
