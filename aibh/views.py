from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Product, Country,AffiliateLink
from decimal import Decimal
import random
from .models import Profile,Panier,Achat,AvisClient
import stripe
import paypalrestsdk
import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from decimal import Decimal
import random
import string
from django.shortcuts import render, redirect
from django.conf import settings
import paypalrestsdk




import stripe
import paypalrestsdk
import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from decimal import Decimal
import random
import string
from django.conf import settings
import stripe
import paypalrestsdk
import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from decimal import Decimal

def index(request):
    # Récupération des objets Blog et Product avec tri inverse
    blogs = Blog.objects.all().order_by('-created_at')  # Tri des blogs du plus récent au plus ancien
    products = Product.objects.all().order_by('-created_at')  # Tri des produits du plus récent au plus ancien
    avis_autorises = AvisClient.objects.filter(autorise=True)
    
    # Récupération des catégories
    categories = list(Category.objects.values('id', 'name'))  # Convertir en liste de dictionnaires

    # Préparation du contexte pour le template
    context = {
        'blogs': blogs,
        'products': products,
        'categories': categories,  # Liste des catégories
        'avis_autorises': avis_autorises,  # Ajout des avis autorisés au contexte
    }
    
    return render(request, 'index.html', context)

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def boutique(request):
    # Récupération des objets Blog et Product avec tri inverse
    blogs = Blog.objects.all().order_by('-created_at')  # Tri des blogs du plus récent au plus ancien
    products = Product.objects.all().order_by('-created_at')  # Tri des produits du plus récent au plus ancien

    # Récupération des catégories
    categories = list(Category.objects.values('id', 'name'))  # Convertir en liste de dictionnaires

    # Initialiser le compteur de produits dans le panier à zéro
    panier_count = 0

    if request.user.is_authenticated:
        # Récupération du profil de l'utilisateur connecté
        profile = get_object_or_404(Profile, user=request.user)
        
        # Compter le nombre de produits dans le panier de l'utilisateur
        panier_count = Panier.objects.filter(profile=profile).count()

    # Préparation du contexte pour le template
    context = {
        'blogs': blogs,
        'products': products,
        'categories': categories,  # Liste des catégories
        'panier_count': panier_count,  # Nombre de produits dans le panier
    }
    
    return render(request, 'boutique.html', context)



# views.py
from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})





from django.shortcuts import render, redirect
from .models import Product, Blog, Category
# views.py
from django.shortcuts import render, redirect
from .models import Blog, Product, Category,AvisClient

def admin_panelle(request):
    if request.method == 'POST':
        # Gestion de l'ajout de produit
        if 'add_product' in request.POST:
            name = request.POST.get('name')
            category_id = request.POST.get('category')
            description = request.POST.get('description')
            price_commercial = request.POST.get('price_commercial')
            price_partner = request.POST.get('price_partner')
            image = request.FILES.get('image')
            product_type = request.POST.get('product_type')
            marge = request.POST.get('marge')
            prix_livraison = request.POST.get('prix_livraison')
            country_id = request.POST.get('country') if product_type == 'foreign' else None

            category = Category.objects.get(id=category_id)
            country = Country.objects.get(id=country_id) if country_id else None

            Product.objects.create(
                name=name,
                category=category,
                description=description,
                price_commercial=price_commercial,
                price_partner=price_partner,
                image=image,
                product_type=product_type,
                country=country,
                marge=marge,
                prix_livraison=prix_livraison
            )
            return redirect('aibh:admin_panelle')

        # Gestion de l'ajout de blog
        elif 'add_blog' in request.POST:
            title = request.POST.get('title')
            category_id = request.POST.get('category')
            description = request.POST.get('description')
            image = request.FILES.get('image')

            category = Category.objects.get(id=category_id)

            Blog.objects.create(
                title=title,
                category=category,
                description=description,
                image=image
            )
            return redirect('aibh:admin_panelle')
        
         # Gestion de l'autorisation des avis
        elif 'update_avis' in request.POST:
            for key, value in request.POST.items():
                if key.startswith('avis_'):
                    avis_id = key.split('_')[1]
                    autorise = value == 'on'
                    try:
                        avis = AvisClient.objects.get(id=avis_id)
                        avis.autorise = autorise
                        avis.save()
                    except AvisClient.DoesNotExist:
                        pass

        # Gérer les autres cas...

    # Préparation du contexte pour le template
    countries = Country.objects.all()
    blogs = Blog.objects.all().order_by('-created_at')
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    avis_clients = AvisClient.objects.all()
    achats = Achat.objects.all().order_by('-created_at')  # Ajout de la récupération des achats
    product_type_choices = Product.PRODUCT_TYPE_CHOICES

    context = {
        'blogs': blogs,
        'products': products,
        'categories': categories,
        'countries': countries,
        'achats': achats,
        'product_type_choices': product_type_choices,
        'avis_clients': avis_clients,  # Ajout des avis au contexte
    }
    
    return render(request, 'admin.html', context)



# views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Blog, Product

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('aibh:admin_panelle')

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('aibh:admin_panelle')



from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Product, Category

def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.category = Category.objects.get(id=request.POST.get('category'))
        blog.description = request.POST.get('description')
        if 'image' in request.FILES:
            blog.image = request.FILES.get('image')
        blog.save()
        return redirect('aibh:admin_panelle')

    categories = Category.objects.all()
    context = {
        'blog': blog,
        'categories': categories
    }
    return render(request, 'admin.html', context)



def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.category = Category.objects.get(id=request.POST.get('category'))
        product.description = request.POST.get('description')
        product.price_commercial = request.POST.get('price_commercial')
        product.price_partner = request.POST.get('price_partner')
        if 'image' in request.FILES:
            product.image = request.FILES.get('image')
        product.save()
        return redirect('aibh:admin_panelle')

    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories
    }
    return render(request, 'admin.html', context)


from django.shortcuts import render
from .models import Blog, Product, Category

def bienetre(request):
    # Récupération des catégories
    categories = Category.objects.all()
    avis_autorises = AvisClient.objects.filter(autorise=True)

    # Vérification si une catégorie a été sélectionnée
    category_id = request.GET.get('category_id')
    if category_id:
        selected_category = Category.objects.get(id=category_id)
        blogs = Blog.objects.filter(category=selected_category).order_by('-created_at')
        products = Product.objects.filter(category=selected_category).order_by('-created_at')
    else:
        blogs = Blog.objects.all().order_by('-created_at')
        products = Product.objects.all().order_by('-created_at')

    context = {
        'blogs': blogs,
        'products': products,
        'categories': categories,
        'avis_autorises':avis_autorises,
        'selected_category': selected_category if category_id else None,
    }
    
    return render(request, 'bienetre.html', context)






from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import paypalrestsdk
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from decimal import Decimal




from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        # Sauvegarde du message
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message_content
        )

        messages.success(request, 'Votre message a été envoyé avec succès!')
        return redirect('aibh:boutique')  # Remplacez 'contact' par l'URL name de la page de contact

    return render(request, 'index.html')








from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            return redirect('aibh:admin_panelle')  # Rediriger vers le panneau d'administration
    return HttpResponse(status=400)  # Mauvaise requête si le nom n'est pas fourni


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profile  # Importez le modèle Profile ici
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        numero_de_telephone = request.POST['numero_de_telephone']
        is_affilie = request.POST.get('is_affilie', False) == 'on'
        photo = request.FILES.get('photo')  # Récupère la photo depuis le formulaire

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà pris.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            profile = Profile(
                user=user, 
                nom=nom, 
                prenom=prenom, 
                numero_de_telephone=numero_de_telephone, 
                is_affilie=is_affilie, 
                photo=photo  # Ajout de la photo au profil
            )
            profile.save()
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('aibh:index')  # Redirigez vers la page d'accueil après l'inscription.

    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        numero_de_telephone = request.POST['numero_de_telephone']
        password = request.POST['password']

        try:
            profile = Profile.objects.get(numero_de_telephone=numero_de_telephone)
            user = authenticate(username=profile.user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('aibh:user_profile_view')  # Redirige vers la page d'accueil après la connexion
            else:
                messages.error(request, "Numéro de téléphone ou mot de passe incorrect.")
        except Profile.DoesNotExist:
            messages.error(request, "Numéro de téléphone ou mot de passe incorrect.")

    return render(request, 'signin.html')



from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout

def user_profile_view(request):
    if not request.user.is_authenticated:
        return redirect('aibh:signin')

    # Récupération du profil de l'utilisateur
    user_profile = request.user.profile
    profile = get_object_or_404(Profile, user=request.user)
    affiliate_links = AffiliateLink.objects.filter(profile=user_profile)

    for link in affiliate_links:
        # Calculer la commission de 5% en utilisant Decimal
        link.commission = link.product.price_commercial * Decimal('0.05')

    # Exemple de multiplication que vous souhaitez faire
    context = {
        'profile': profile,
        'affiliate_links': affiliate_links,
    }

    
    return render(request, 'compte.html', context)






from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout

from django.shortcuts import render, get_object_or_404




from decimal import Decimal








from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Achat)
def post_achat_save(sender, instance, **kwargs):
    instance.process_affiliate_commission()
















from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages



from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

def ajouter_au_panier(request, product_id):
    if not request.user.is_authenticated:
        return redirect('aibh:signin')

    product = get_object_or_404(Product, id=product_id)
    user = request.user
    profile = get_object_or_404(Profile, user=user)

    aff_id = request.GET.get('aff_id')
    affiliate_link = None

    if aff_id:
        affiliate_link = get_object_or_404(AffiliateLink, token=aff_id)

    # Détermine le prix en fonction du type d'utilisateur et du type de produit
    if profile.is_affilie:
        price = product.price_partner
    else:
        price = product.price_commercial

    # Ajoute la marge si le produit est étranger
    if product.product_type == 'foreign':
        price += product.marge

    # Ajoute ou met à jour l'article dans le panier
    panier_item, created = Panier.objects.get_or_create(
        profile=profile,
        product=product,
        defaults={'price': price, 'affiliate_link': affiliate_link}
    )

    if not created:
        panier_item.quantity += 1
        panier_item.price += price
        panier_item.save()

    messages.success(request, f"{product.name} a été ajouté à votre panier.")
    
    return redirect('aibh:boutique')


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def custom_logout(request):
    logout(request)  # Déconnecter l'utilisateur
    return redirect('aibh:index')  # Rediriger vers la page d'accueil


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def toggle_affiliation(request):
    if request.method == 'POST':
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        
        # Inverse l'état de l'affiliation
        profile.is_affilie = not profile.is_affilie
        profile.save()

        # Retourner une réponse JSON pour informer le front-end
        return JsonResponse({'success': True, 'is_affilie': profile.is_affilie})
    return JsonResponse({'success': False}, status=400)










import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Panier, Profile, Achat



# views.py








def afficher_panier(request):
    if not request.user.is_authenticated:
        return redirect('aibh:signin')

    profile = get_object_or_404(Profile, user=request.user)
    panier_items = Panier.objects.filter(profile=profile)
    total = Panier.total_panier(profile)

    context = {
        'panier_items': panier_items,
        'total': total,
        'customer_name': profile.nom,
        'customer_surname': profile.prenom,
        'customer_phone_number': profile.numero_de_telephone,
        'customer_email': request.user.email,
    }

    return render(request, 'panier.html', context)




from django.shortcuts import redirect
from django.contrib import messages

def vider_panier(request):
    if not request.user.is_authenticated:
        return redirect('aibh:signin')

    profile = get_object_or_404(Profile, user=request.user)
    Panier.objects.filter(profile=profile).delete()

    messages.success(request, "Votre panier a été vidé avec succès.")
    return redirect('aibh:afficher_panier')





from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Achat, Panier, Profile

@login_required
def enregistrer_achat(request):
    if request.method == "POST":
        profile = get_object_or_404(Profile, user=request.user)
        item_id = request.POST.get('item_id')
        transaction_id = request.POST.get('transaction_id')
        payment_status = request.POST.get('payment_status')
        
        # Récupération de l'élément du panier correspondant
        panier_item = get_object_or_404(Panier, id=item_id, profile=profile)

        # Création d'un nouvel enregistrement d'achat
        Achat.objects.create(
            profile=profile,
            panier=panier_item,
            payment_method="CinetPay",  # Tu peux personnaliser ou rendre dynamique ce champ
            payment_status=payment_status,
            transaction_id=transaction_id,
        )

        # Optionnel : Mettre à jour le statut du panier ou supprimer l'item si nécessaire
        panier_item.payment_status = payment_status
        panier_item.save()

        # Redirection vers une page de confirmation ou le panier
        return redirect('aibh:panier')

    # Si la méthode n'est pas POST, on redirige vers le panier (sécurité supplémentaire)
    return redirect('aibh:panier')





from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Profile, AffiliateLink

from django.urls import reverse



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def generate_affiliate_link(request, product_id):
    if not request.user.is_authenticated:
        return redirect('aibh:signin')

    profile = get_object_or_404(Profile, user=request.user)
    product = get_object_or_404(Product, id=product_id)

    if not profile.is_affilie:
        messages.error(request, "Vous devez être affilié pour générer des liens.")
        return redirect('aibh:boutique')

    affiliate_link, created = AffiliateLink.objects.get_or_create(profile=profile, product=product)

    messages.success(request, f"Lien d'affiliation généré: {affiliate_link.get_affiliate_url()}")
    return redirect('aibh:user_profile_view')




from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})


def get_affiliate_url(self):
    try:
        product_url = self.product.get_absolute_url()
    except NoReverseMatch:
        product_url = '#'
    return f"{product_url}?aff_id={self.token}"




from django.shortcuts import render
from .models import Product

def foreign_products_view(request):
    foreign_products = Product.objects.filter(product_type=Product.FOREIGN)
    return render(request, 'foreign_products.html', {'products': foreign_products})



def local_products_view(request):
    local_products = Product.objects.filter(product_type=Product.LOCAL)
    return render(request, 'local_products.html', {'products': local_products})



from django.shortcuts import render, redirect
from .models import Product, AvisClient
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import AvisClient, Profile



from django.shortcuts import render, redirect
from .models import AvisClient, Profile

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AvisClient, Profile

def soumettre_avis(request):
    if not request.user.is_authenticated:
        return redirect('aibh:signin')
    
    if request.method == 'POST':
        message = request.POST.get('message')

        # Récupère le profil de l'utilisateur actuellement connecté
        profile = Profile.objects.get(user=request.user)

        AvisClient.objects.create(
            profile=profile,
            message=message
        )

        return redirect('aibh:index')  # Redirige vers la page d'accueil après soumission

    return render(request, 'soumettre_avis.html')
