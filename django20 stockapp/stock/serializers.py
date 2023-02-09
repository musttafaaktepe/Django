from rest_framework import serializers
from .models import Category, Brand, Product, Firm, Purchases, Sales


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()  # read_only
    
    class Meta:
        model = Category
        fields =  "__all__"
        
    def get_product_count(self, obj):
        return Product.objects.filter(category_id=obj.id).count()
    

class ProductSerializer(serializers.ModelSerializer):

    category=serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    
    
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "category_id",
            "brand",
            "brand_id",
            "stock",
        )
        read_only_fields =("stock",)


class CategoryProductSerializer(serializers.ModelSerializer):
    
    products = ProductSerializer(many=True)
    product_count = serializers.SerializerMethodField()  # read_only
    
    class Meta:
        model = Category
        fields = ("id", "name", "product_count", "products")
        
    def get_product_count(self, obj):
        return Product.objects.filter(category_id=obj.id).count()

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'image'
        )


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            'id',
            'name',
            'phone',
            'image',
            'address'
        )

class PurchasesSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField() 
    firm = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    firm_id = serializers.IntegerField()
    category = serializers.SerializerMethodField()
    tiime_hour

    class Meta:
        model = Purchases
        fields = (
            "id",
            "user",
            "user_id",
            "category",
            "firm",
            "firm_id",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "quantity",
            "price",
            "price_total",
            # "createds",
            "time_hour",?????????
            "updated",
        )
    
    # def get_category(self, obj):
    #     product = Product.objects.get(id=obj.product_id)
    #     return Category.objects.get(id=product.category_id).name
    
    def get_category(self, obj):
        return obj.product.category.name
    
    def tiime_hour(self, obj):
        return datetime.datetime.strftime(obj.createds, "%H:%M")


