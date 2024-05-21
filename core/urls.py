
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ListarPropiedad, CrearPropiedad, EliminarPropiedad, ActualizarPropiedad,DetallePropiedad, descargar_pdf
urlpatterns = [
    path('', views.home, name="home"),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/',views.registro, name='registro'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('mostrar/', ListarPropiedad.as_view(), name='mostrar'),
    path('agregar/', CrearPropiedad.as_view(), name='agregar'),
    path('eliminar/<int:pk>/', EliminarPropiedad.as_view(), name='eliminar_propiedad'),
    path('actualizar/<int:pk>/', ActualizarPropiedad.as_view(), name='actualizar_propiedad'),
    path('detalle/<int:pk>/', DetallePropiedad.as_view(), name='detalle'),
    path('descargar_pdf/<int:pk>/', views.descargar_pdf, name='descargar_pdf')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
