from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet, login_view
from .views import ProductoViewSet, ProductoDetailView
from .views import register_view

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('api/', include(router.urls)),
    path('productos/', ProductoViewSet.as_view({'get': 'list', 'post': 'create'}), name='productos-list'),
    path('productos/<int:id>/', ProductoDetailView.as_view(), name='producto-detail'),
    # Resto de las rutas de la aplicación
]