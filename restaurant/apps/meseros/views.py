
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.meseros.serializers import MeserosSerializer
from .models import Meseros
from .form import MeserosForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.core import serializers as ssr
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def inicio(request):
    return render(request, 'pagina/inicio.html')

def meseros(request):
    meseros_list = Meseros.objects.all()
    context = {'meseros': meseros_list}
    return render(request, 'meseros/meseros.html', context)

def crear(request):
    formulario = MeserosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('meseros')
    return render(request, 'meseros/crear.html', {'formulario': formulario})

def eliminar(request, id):
    meseros = Meseros.objects.get(id=id)
    meseros.delete()
    return redirect('meseros')

def editar(request, id):
    meseros_list = meseros.objects.get(id=id)
    formulario = MeserosForm(request.POST or None, request.FILES or None, instance=meseros_list)
    context = {'formulario': formulario}
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('meseros')
    return render(request, 'meseros/editar.html', context)

class MeserosList(ListView):
    model = Meseros
    template_name = 'meseros/meseros_vc.html'

class MeserosCreate(CreateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros/crear.html'
    success_url = reverse_lazy('meseros_list_vc')

class MeserosUpdate(UpdateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros/editar_vc.html'
    success_url = reverse_lazy('meseros_list_vc')

class MeserosDelete(DeleteView):
    model = Meseros
    template_name = 'meseros/eliminar_vc.html'
    success_url = reverse_lazy('meseros_list_vc')


# Serializacion con Django
def listMeserosSerializer(request):
    list_meseros = ssr.serialize('json', meseros.objects.all())
    return HttpResponse(list_meseros, content_type='application/json')


# Serializacion con Django Rest Framework
class MeserosApiView(ListAPIView):
    queryset = meseros.objects.all()
    serializer_class = MeserosSerializer


# Serializacion con Django Rest Framework Funciones
@api_view(['GET', 'POST'])
def meseros_api_view(request):

    if request.method == 'GET':
        queryset = Meseros.objects.all()
        serializer_class = MeserosSerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MeserosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def meseros_detail_view(request, pk):
    queryset = Meseros.objects.filter(id=pk).first()
    if queryset:
        if request.method == 'GET':
            #queryset = Meseros.objects.filter(id=pk).first()
            serializer_class = MeserosSerializer(queryset)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            #queryset = Meseros.objects.filter(id=pk).first()
            serializer_class = MeserosSerializer(queryset, data=request.data)

            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_200_OK)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            #queryset = Meseros.objects.filter(id=pk).first()
            queryset.delete()
            return Response({'message': 'Mesero eliminado correctamente'}, status=status.HTTP_200_OK)
    return Response({'message': 'No se encuentra el Mesero'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def meseros_update_view(request, pk):
    queryset = Meseros.objects.filter(id=pk).first()
    if queryset:
        if request.method == 'PUT':
            #queryset = Meseros.objects.filter(id=pk).first()
            serializer_class = MeserosSerializer(queryset, data=request.data)

            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_200_OK)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'No se encuentra el Mesero'}, status=status.HTTP_400_BAD_REQUEST)
