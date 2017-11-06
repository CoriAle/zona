from django.conf.urls import url
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate,delete_solicitud

urlpatterns = [
    url(r'^index$', index_adopcion),
    url(r'^solicitud/listar$', SolicitudList, name='solicitud_listar'),
    url(r'^solicitud/nueva$', SolicitudCreate.as_view(), name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^solicitud/borrar/(?P<id_solicitud>\d+)/$', delete_solicitud, name='solicitud_delete'),
]
