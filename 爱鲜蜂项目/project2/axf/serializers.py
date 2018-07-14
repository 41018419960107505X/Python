
from rest_framework import serializers
from axf.models import SlideShow, MainDescription, Product

class SlideShowSerializer(serializers.ModelSerializer):
    class Meta():
        model = SlideShow
        fields = ("id", "trackid", "name", "img", "sort")

class MainDescriptionSerializer(serializers.ModelSerializer):
    class Meta():
        model = MainDescription
        fields = ("categoryId", "categoryName", "sort", "img")

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = ("categoryId", "productId")