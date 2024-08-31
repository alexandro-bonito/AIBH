
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'aibh'



urlpatterns = [
    path('', views.index, name='index'),
    path('admin_panelle/', views.admin_panelle, name='admin_panelle'),
    path('admin_panelle/', views.admin_panelle, name='admin_panelle'),
    path('blog/delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('blog/edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('boutique/', views.boutique, name='boutique'),
    path('bienetre/', views.bienetre, name='bienetre'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('user_profile_view/', views.user_profile_view, name='user_profile_view'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('add-category/', views.add_category, name='add_category'),
    path('panier/', views.afficher_panier, name='afficher_panier'),
    path('logout/', views.custom_logout, name='logout'),
    path('vider-panier/', views.vider_panier, name='vider_panier'),
    path('toggle-affiliation/', views.toggle_affiliation, name='toggle_affiliation'),
    path('ajouter_au_panier/<int:product_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.afficher_panier, name='panier_view'),
    path('enregistrer-achat/', views.enregistrer_achat, name='enregistrer_achat'),
    path('soumettre-avis/', views.soumettre_avis, name='soumettre_avis'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('generate-affiliate-link/<int:product_id>/', views.generate_affiliate_link, name='generate_affiliate_link'),
    path('produits-etrangers/', views.foreign_products_view, name='foreign_products'),
    path('produits-locaux/', views.local_products_view, name='local_products'),


 
]
