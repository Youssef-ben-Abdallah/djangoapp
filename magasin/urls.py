from xml.etree.ElementInclude import include
from django.urls import path
from .views import CategoryAPIView,ProduitAPIView
from magasin.views import ProductViewset, CategoryAPIView
from . import views
#from rest_framework import routers
#router = routers.SimpleRouter()
#router.register('produit', ProductViewset, basename='produit')
urlpatterns = [
    path('',views.index,name='index'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('addcommande/', views.addcommande, name='addcommande'),
    path('addfournisseur/', views.addfournisseur, name='addfournisseur'),
    path('search/', views.search, name='search'),
    path('produit/<int:produit_id>/', views.produit_detail, name='produit_detail'),
    path('categories/', views.categorie_list, name='categorie_list'),
    path('categorie/<int:categorie_id>/', views.categorie_detail, name='categorie_detail'),
    path('fournisseur/<int:fournisseur_id>/', views.fournisseur_detail, name='fournisseur_detail'),
    path('fournisseurs/', views.fournisseur_list, name='fournisseur_list'),
    path('commande/<int:commande_id>/', views.commande_detail, name='commande_detail'),
    path('commande/', views.commande_list, name='commande_list'),
    path('register/',views.register, name = 'register'), 
    path('login/', views.login_view, name='login_view'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/product/', ProduitAPIView.as_view()),
    path('api/produit/<int:categorie>', views.ProduitAPIView.as_view()),
    #path('api/', include(router.urls)),
]
