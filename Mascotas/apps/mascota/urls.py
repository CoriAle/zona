from django.conf.urls import url
from apps.mascota.views import index, mascota_view, mascotas_list, mascota_edit, delete_mascota,\
MascotaList
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^nuevo$', login_required(mascota_view), name="crear"),
    url(r'^mascotas$', login_required(MascotaList.as_view()), name="mascotas_list"),
    url(r'^editar/(?P<id_mascota>[0-9]+)/$', login_required(mascota_edit), name="mascotas_editar"),
    url(r'^eliminar/(?P<id_mascota>[0-9]+)/$', login_required(delete_mascota), name="mascotas_eliminar"),
=======
=======
>>>>>>> 453d06fa7a562420a537d523af16025ce578dc61

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^nuevo$', mascota_view, name="crear"),
    url(r'^mascotas$', MascotaList.as_view(), name="mascotas_list"),
    url(r'^editar/(?P<id_mascota>[0-9]+)/$', mascota_edit, name="mascotas_editar"),
    url(r'^eliminar/(?P<id_mascota>[0-9]+)/$', delete_mascota, name="mascotas_eliminar"),
<<<<<<< HEAD
>>>>>>> origin/master
=======
>>>>>>> 453d06fa7a562420a537d523af16025ce578dc61

]
