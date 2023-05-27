from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import viewsets, routers
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductoSerializer
from rest_framework.generics import RetrieveAPIView
from .models import Producto
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Autenticación exitosa, iniciar sesión
            login(request, user)
            return redirect('api-root')  # Redirigir al usuario a la ruta deseada
        else:
            # Autenticación fallida, mostrar mensaje de error
            error_message = "Credenciales inválidas. Inténtalo de nuevo."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            # Verificar si el usuario ya existe
            user = User.objects.get(username=username)
            error_message = "El usuario ya existe. Intente con otro nombre de usuario."
            return render(request, 'register.html', {'error_message': error_message})
        except User.DoesNotExist:
            # Crear el superusuario
            user = User.objects.create_superuser(username=username, password=password)
            user.save()
            return redirect('login')  # Redirigir al usuario al inicio de sesión
    else:
        return render(request, 'register.html')