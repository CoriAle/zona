from django.conf.urls import url
from apps.mascota.views import index, mascota_view, mascotas_list, mascota_edit, delete_mascota,\
MascotaList
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^nuevo$', login_required(mascota_view), name="crear"),
    url(r'^mascotas$', login_required(MascotaList.as_view()), name="mascotas_list"),
    url(r'^editar/(?P<id_mascota>[0-9]+)/$', login_required(mascota_edit), name="mascotas_editar"),
    url(r'^eliminar/(?P<id_mascota>[0-9]+)/$', login_required(delete_mascota), name="mascotas_eliminar"),

]
