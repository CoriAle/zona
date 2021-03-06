from django.conf.urls import url
from apps.mascota.views import index, mascota_view, mascotas_list, mascota_edit, delete_mascota,\
MascotaList, vacuna_view, vacuna_edit, delete_vacuna, vacuna_list, mascota_detalle

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^nuevo$', login_required(mascota_view), name="crear"),
    url(r'^vacuna/nueva$', login_required(vacuna_view), name="crearvacuna"),
    url(r'^mascotas$', login_required(mascotas_list), name="mascotas_list"),
    url(r'^vacunas$', login_required(vacuna_list), name="vacuna_list"),
    url(r'^editar/(?P<id_mascota>[0-9]+)/$', login_required(mascota_edit), name="mascotas_editar"),
    url(r'^vacuna/editar/(?P<id_vacuna>[0-9]+)/$', login_required(vacuna_edit), name="vacuna_editar"),
    url(r'^eliminar/(?P<id_mascota>[0-9]+)/$', login_required(delete_mascota), name="mascotas_eliminar"),
    url(r'^vacuna/eliminar/(?P<id_vacuna>[0-9]+)/$', login_required(delete_vacuna), name="vacuna_eliminar"),
    url(r'^detalle/(?P<id_mascota>[0-9]+)/$', login_required(mascota_detalle), name="mascota_det"),
]
