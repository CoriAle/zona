from django.conf.urls import url
from apps.mascota.views import index, mascota_view, mascotas_list, mascota_edit, delete_mascota

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^nuevo$', mascota_view, name="crear"),
    url(r'^mascotas$', mascotas_list, name="mascotas_list"),
    url(r'^editar/(?P<id_mascota>[0-9]+)/$', mascota_edit, name="mascotas_editar"),
    url(r'^eliminar/(?P<id_mascota>[0-9]+)/$', delete_mascota, name="mascotas_eliminar"),

]
