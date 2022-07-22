from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import DocenteList, DocenteCreate, DocenteUpdate , DocenteDelete
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('listar/', DocenteList.as_view(), name="docentes_list"),
    # localhost:8000/Docente/crear
    path('crear/', DocenteCreate.as_view(), name="docentes_form"),
    path('editar/<int:pk>', DocenteUpdate.as_view(), name="docentes_update"),
    path('borrar/<int:pk>', DocenteDelete.as_view(), name="docentes_borrar"),
    path('api/', API_objects.as_view()),
    path('api/<int:pk>/', API_objects_details.as_view()),
]
 
urlpatterns = format_suffix_patterns(urlpatterns)

