from django.contrib import admin

from .models import Product, ActiveIngredient, ToxicityLabel, Type, Formulation


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cod_senasa', 'is_trazable')
    ordering = ('-is_trazable',)
    search_fields = ('name', 'cod_senasa')


admin.site.register(ActiveIngredient)
admin.site.register(ToxicityLabel)
admin.site.register(Type)
admin.site.register(Formulation)
