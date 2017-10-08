from django.conf.urls import url
from apps.mascota.views import index, mascota_view, mascotas_list, mascota_edit

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^nuevo$', mascota_view, name="crear"),
    url(r'^mascotas$', mascotas_list, name="mascotas_list"),
    url(r'^e/(?P<id>\d+)$', mascota_edit, name="mascotas_editar"),
]
