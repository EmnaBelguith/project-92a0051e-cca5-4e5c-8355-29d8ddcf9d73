# mydjangoproject/myapp/urls.py
from django.urls import path
from . import views # <-- Ici, vous importez 'views' depuis le même dossier (myapp)

urlpatterns = [
    path('', views.index, name='index'), # Le chemin vide '' signifie la racine de cette application (ex: /myapp/)
]