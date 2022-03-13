from django.contrib import admin

from .models import Product, ActiveIngredient, ToxicityLabel, Type, Formulation

admin.site.register(Product)
admin.site.register(ActiveIngredient)
admin.site.register(ToxicityLabel)
admin.site.register(Type)
admin.site.register(Formulation)