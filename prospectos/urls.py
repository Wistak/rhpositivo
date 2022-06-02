from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('prospectos', views.prospectos, name='prospectos'),
    path('nuevo_prospecto', views.nuevoProspecto, name='nuevo_prospecto'),
    path('evaluar_prospecto/<str:pk>/', views.evaluarProspecto, name="evaluar_prospecto"),
    re_path(r'^media/(?P<file_name>.+)$', views.download),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
)