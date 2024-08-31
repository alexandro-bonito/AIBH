from django.db import models
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User  # Importation du modèle User
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from decimal import Decimal


from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    numero_de_telephone = models.CharField(max_length=15, unique=True)
    is_affilie = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='media/', null=True, blank=True)  # Ajout de la photo

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)  # Date et heure de création avec valeur par défaut

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    LOCAL = 'local'
    FOREIGN = 'foreign'
    PRODUCT_TYPE_CHOICES = [
        (LOCAL, 'Local'),
        (FOREIGN, 'Étranger'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price_commercial = models.DecimalField(max_digits=10, decimal_places=2)
    price_partner = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(default=timezone.now)
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE_CHOICES, default=LOCAL)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    marge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prix_livraison = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('aibh:product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

    def final_commercial_price(self):
        marge = self.marge if self.marge is not None else Decimal('0.00')
        prix_livraison = self.prix_livraison if self.prix_livraison is not None else Decimal('0.00')
        return self.price_commercial + marge + prix_livraison

    def total_price(self):
        marge = self.marge if self.marge is not None else Decimal('0.00')
        prix_livraison = self.prix_livraison if self.prix_livraison is not None else Decimal('0.00')
        return self.price_commercial + marge + prix_livraison








from django.db import models
import secrets
from django.db import models
import secrets

class AffiliateLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)
    token = models.CharField(max_length=64, unique=True, editable=False)  # Jeton sécurisé
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_hex(32)  # Génère un jeton de 64 caractères hexadécimaux
        super().save(*args, **kwargs)

    def get_affiliate_url(self):
        return f"{self.product.get_absolute_url()}?aff_id={self.token}"

    def __str__(self):
        return f"Affilié: {self.profile.user.username} - Produit: {self.product.name}"



class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    created_at = models.DateTimeField(default=timezone.now)  # Date et heure de création avec valeur par défaut

    def __str__(self):
        return self.title



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"




from django.db import models

class Panier(models.Model):
    STATUS_CHOICES = [
        ('PAID', 'Payé'),
        ('PENDING', 'En cours'),
        ('UNPAID', 'Non payé'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)  # Liaison avec Profile
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='paniers')  # Relation unique au panier
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)
    affiliate_link = models.ForeignKey(AffiliateLink, on_delete=models.SET_NULL, null=True, blank=True)
    payment_status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default='UNPAID',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.quantity} x {self.product.name} - {self.profile.nom} {self.profile.prenom}"

    def total_price(self):
        return self.quantity * self.price

    @classmethod
    def total_panier(cls, profile):
        panier_items = cls.objects.filter(profile=profile)
        total = sum(item.total_price() for item in panier_items)
        return total



from django.db import models
# models.py

from django.db import models
from decimal import Decimal

class Achat(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20)  # Moov, Orange Money, etc.
    payment_status = models.CharField(max_length=10)  # PAID, FAILED, PENDING
    transaction_id = models.CharField(max_length=100)  # ID transaction API
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Achat de {self.profile.nom} {self.profile.prenom} - {self.panier.product.name}"

    def process_affiliate_commission(self):
        # Récupérer les produits dans le panier
        produits = self.panier.products.all()

        for produit in produits:
            # Vérifier s'il y a un lien affilié pour ce produit
            affiliate_link = AffiliateLink.objects.filter(product=produit).first()
            if affiliate_link:
                # Récupérer le wallet du profil associé à ce lien affilié
                wallet = Wallet.objects.get(profile=affiliate_link.profile)

                # Calculer la commission (5%)
                commission = produit.price_commercial * Decimal('0.05')

                # Ajouter la commission au solde du wallet
                wallet.balance += commission
                wallet.last_commission = commission
                wallet.save()




class AvisClient(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    autorise = models.BooleanField(default=False)  # Champ pour indiquer si l'avis est autorisé
    date = models.DateTimeField(auto_now_add=True)  # Date de création de l'avis

    def __str__(self):
        return f"Avis de {self.profile.nom} {self.profile.prenom} - Autorisé: {self.autorise}"