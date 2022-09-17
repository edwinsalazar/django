
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.clientes.serializers import ClienteSerializer
from .models import Cliente
from .form import ClienteForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.core import serializers as ssr
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def inicio(request):
    return render(request, 'pagina/inicio.html')

def clientes(request):
    clientes_list = Cliente.objects.all()
    context = {'clientes': clientes_list}
    return render(request, 'clientes/clientes.html', context)

def crear(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/crear.html', {'formulario': formulario})

def eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')


def editar(request, id):
    clientes_list = Cliente.objects.get(id=id)
    formulario = ClienteForm(request.POST or None, request.FILES or None, instance=clientes_list)
    context = {'formulario': formulario}
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/editar.html', context)


class ClienteList(ListView):
    model = Cliente
    template_name = 'clientes/cliente_vc.html'


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/crear.html'
    success_url = reverse_lazy('cliente_list_vc')


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/editar_vc.html'
    success_url = reverse_lazy('cliente_list_vc')


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'clientes/eliminar_vc.html'
    success_url = reverse_lazy('cliente_list_vc')


# Serializacion con Django
def listClienteSerializer(request):
    list_clientes = ssr.serialize('json', Cliente.objects.all())
    return HttpResponse(list_clientes, content_type='application/json')


# Serializacion con Django Rest Framework
class ClienteApiView(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


# Serializacion con Django Rest Framework Funciones
@api_view(['GET', 'POST'])
def cliente_api_view(request):

    if request.method == 'GET':
        queryset = Cliente.objects.all()
        serializer_class = ClienteSerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def cliente_detail_view(request, pk):
    queryset = Cliente.objects.filter(id=pk).first()
    if queryset:
        if request.method == 'GET':
            #queryset = Cliente.objects.filter(id=pk).first()
            serializer_class = ClienteSerializer(queryset)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            #queryset = Cliente.objects.filter(id=pk).first()
            serializer_class = ClienteSerializer(queryset, data=request.data)

            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_200_OK)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            #queryset = Cliente.objects.filter(id=pk).first()
            queryset.delete()
            return Response({'message': 'Cliente eliminado correctamente'}, status=status.HTTP_200_OK)
    return Response({'message': 'No se encuentra el cliente'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def cliente_update_view(request, pk):
    queryset = Cliente.objects.filter(id=pk).first()
    if queryset:
        if request.method == 'PUT':
            #queryset = Cliente.objects.filter(id=pk).first()
            serializer_class = ClienteSerializer(queryset, data=request.data)

            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=status.HTTP_200_OK)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'No se encuentra el cliente'}, status=status.HTTP_400_BAD_REQUEST)
