from rest_framework import serializers

from .models import Product, Category, Card, CardItem, Order, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'parent', 'url']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['user', 'status']


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'id', 'img','name',]

class CardItemSerializer(serializers.ModelSerializer):
    product = ImgSerializer(read_only=True)

    class Meta:
        model = CardItem
        fields = ['id', 'product', 'quantity', 'price_sum', ]


class SaveCardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['card']


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['card', 'status', 'date']


class ChangeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardItem
        fields = ['quantity']


class AddCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['product', 'text']


class ChangeCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    comment = AddCommentSerializers(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'img', 'comment' ]


class ProductSerializerall(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    comment_count = serializers.IntegerField(source="get_count_comments", read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'img', 'comment_count' ]