# mydjangoproject/myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp import views # <-- AJOUTEZ OU DÉCOMMENTEZ CETTE LIGNE POUR IMPORTER LA VUE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')), # Gardez cette ligne si vous voulez aussi /myapp/
    path('', views.index, name='home'), # <-- AJOUTEZ OU DÉCOMMENTEZ CETTE LIGNE POUR MAPPER LA RACINE
]