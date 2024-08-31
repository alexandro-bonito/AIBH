from django.db import models


from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Blog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_commercial', 'price_partner')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title',)





















from django.contrib import admin
from .models import Product



from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)


from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



from django.contrib import admin
from .models import Profile

from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'user', 'numero_de_telephone', 'is_affilie')
    search_fields = ('nom', 'prenom', 'numero_de_telephone', 'user__username')
    ordering = ('nom', 'prenom')
    fieldsets = (
        (None, {
            'fields': ('user', 'nom', 'prenom', 'numero_de_telephone')
        }),
        ('Statut', {
            'fields': ('is_affilie',)  # Ajout d'une virgule pour créer un tuple
        }),
    )

admin.site.register(Profile, ProfileAdmin)


from django.contrib import admin
from .models import Panier

from django.contrib import admin
from .models import Panier

class PanierAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'display_products')

    def display_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
    display_products.short_description = 'Products'

admin.site.register(Panier, PanierAdmin)



from django.contrib import admin
from .models import AffiliateLink

class AffiliateLinkAdmin(admin.ModelAdmin):
    list_display = ('profile', 'product', 'commission_rate', 'created_at', 'get_affiliate_url')
    list_filter = ('profile__user__username', 'product__name')
    search_fields = ('profile__user__username', 'product__name')
    readonly_fields = ('get_affiliate_url', 'created_at')
    ordering = ('-created_at',)

    def get_affiliate_url(self, obj):
        return obj.get_affiliate_url()
    get_affiliate_url.short_description = "Lien d'affiliation"
    get_affiliate_url.allow_tags = True

admin.site.register(AffiliateLink, AffiliateLinkAdmin)




from django.contrib import admin
from .models import Achat

class AchatAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'panier', 'payment_status', 'transaction_id', 'created_at')
    search_fields = ('profile__nom', 'profile__prenom', 'panier__product__name', 'transaction_id')
    list_filter = ('payment_status', 'payment_method', 'created_at')
    date_hierarchy = 'created_at'

    # Optionnel: afficher les détails d'un achat particulier
    def view_on_site(self, obj):
        return f"/achat/{obj.id}/"  # Lien vers la page de détails de l'achat, si elle existe

admin.site.register(Achat, AchatAdmin)


from django.contrib import admin
from .models import AvisClient




from django.contrib import admin
from .models import AvisClient, Profile

class AvisClientAdmin(admin.ModelAdmin):
    list_display = ('profile', 'message', 'autorise', 'date')
    list_filter = ('autorise', 'date')
    search_fields = ('profile__nom', 'profile__prenom', 'message')

admin.site.register(AvisClient, AvisClientAdmin)
