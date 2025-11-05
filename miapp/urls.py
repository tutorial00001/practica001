from django.urls import path
from . import views
urlpatterns = [
   path ("inicio/",views.inicio, name = "pagPrincipal"),

   path("pagina2/",views.pagina2, name = "pagina2Principito"),

   path("pagina1/",views.pagina1, name = "pag1elPrincipito"),

   path("homer/", views.main, name ="queso"),
]