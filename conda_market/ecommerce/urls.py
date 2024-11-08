from django.urls import path
from . import views

app_name = 'ecommerce'

# Ces urls ont été defini ici pour initialiser le template et le prendre en main car avec le progressement les application seront creer a l'instar 
#de "Produit" panier/cart, paiement,et donc les urls devront etre dans leurs application respectif. actuellemnt c'est juste pour eviter les erreurs
urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
