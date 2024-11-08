"""
URL configuration for conda_market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Importation des vues générales :la page d'accueil,s'il y 'en a mais pour ce cas c'est accessible depuis l'application [ecommerce]


urlpatterns = [
    path('admin/', admin.site.urls), # Administration

    # Page d'accueil

    #path('', views.home, name='home'),

    path('', include('ecommerce.urls', namespace='ecommerce')),

    # URLs des applications
    #path('products/', include('products.urls', namespace='products')),       # Produits (liste, détails, catégories..)
    #path('cart/', include('cart.urls', namespace='cart')),                   # Panier (affichage, checkout..)
    #path('account/', include('account.urls', namespace='account')),          # Comptes (connexion, inscription, profil, réinitialisation mot de passe..)
    #path('orders/', include('orders.urls', namespace='orders')),             # Commandes (historique, détails..)
    #path('payments/', include('payments.urls', namespace='payments')),       # Paiements (processus de paiement, confirmation..)
]


# Gestion des fichiers statiques en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #if we want to create and others folder to storage Media file we can rename it in [media] now we can storage all media in static Folder
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)