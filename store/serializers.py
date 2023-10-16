from rest_framework import serializers

from . import models


class ProductTypeDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductTypeData
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductCategory
        fields = "__all__"


class ProductDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductData
        fields = "__all__"


class ProductDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductDelete
        fields = "__all__"


class AreaDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AreaData
        fields = "__all__"


class ShopDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ShopData
        fields = "__all__"


class InputInvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InputInvoice
        fields = "__all__"


class InputDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InputData
        fields = "__all__"
