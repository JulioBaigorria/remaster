from abc import ABC

from rest_framework import serializers
from .models import ActiveIngredient, Product, Formulation, Type, ToxicityLabel


class ToxicityLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToxicityLabel
        fields = '__all__'


class FormulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulation
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name',)
        read_only_fields = ('name',)


class ActiveIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveIngredient
        fields = ('name', 'created_at',)


class ActiveIngredientListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return value.name


class TypeListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return value.name


class FormulationListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return value.symbol


class ToxicityListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return value.category


class ProductSerializer(serializers.ModelSerializer):
    act_ingredients = ActiveIngredientListingField(many=True, queryset=ActiveIngredient.objects.all())
    types = TypeListingField(many=True, queryset=Type.objects.all())
    formulations = FormulationListingField(many=True, queryset=Formulation.objects.all())
    tox_labels = ToxicityListingField(many=True, queryset=ToxicityLabel.objects.all())

    # formulations = serializers.PrimaryKeyRelatedField(many=True)
    # tox_labels = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Product
        fields = (
            'name', 'cod_senasa', 'act_ingredients', 'types', 'formulations', 'tox_labels', 'is_trazable',)
        # read_only_fields = ('id',)

    # def to_representation(self, instance):
    #     print(TypeSerializer(instance.name))
    #     rep = super().to_representation(instance)
    #     # rep['types'] = TypeSerializer(instance.name).data
    #     return rep

# class ProductDetailSerializer(ProductSerializer):
#     """Serializa Detalle de receta"""
#     types = TypeSerializer(many=True, read_only=True)
#     act_ingredients = ActiveIngredientSerializer(many=True, read_only=True)
#     formulations = FormulationSerializer(many=True, read_only=True)
#     tox_labels = ToxicityLabelSerializer(many=True, read_only=True
#                                          )
#     print()
