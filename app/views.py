# from django.shortcuts import render
# from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from .models import Product, Category, CardItem, Order, Card, Comment
from .serializers import ProductSerializer, CategorySerializer, CardItemSerializer, SaveCardItemSerializer, \
    OrderSerializer, OrderListSerializer, ChangeOrderSerializer, AddCommentSerializers, ChangeCommentSerializers, \
    ProductSerializerall


#
# class ProductListView(View):
#     def get(self, request):
#         products = Product.objects.all()
#         return render(request, 'index.html', {'products': products})


# class CategoryListView(APIView):
#     def get(self, request):
#         category=Category.objects.all()
#         category_ser=CategorySerializer(category, many=True)
#         return Response (category_ser.data)


class CategoryListView(generics.ListAPIView):
    """Показывает все категории"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(APIView):
    """показывает все товары """

    def get(self, request):
        products = Product.objects.all()
        products_ser = ProductSerializerall(products, many=True)
        return Response(products_ser.data)


class ProductDetailView(generics.RetrieveAPIView):
    """подробное описание товара"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FilterCategoryListView(generics.ListAPIView):
    """вывод товаров определенной категории"""
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(category__url=self.kwargs.get("slug"))


class FilterCardListView(generics.ListAPIView):
    """Показывает все товары в текущей корзине"""
    permission_classes = [permissions.IsAuthenticated]  # если авторизован
    serializer_class = CardItemSerializer

    def get_queryset(self):
        return CardItem.objects.filter(card__user=self.request.user, card__status=True)


class AddCartItemViews(generics.CreateAPIView):
    """добавляем товар в корзину"""
    queryset = CardItem.objects.all()
    serializer_class = SaveCardItemSerializer

    def perform_create(self, serializer):  # переопредиляем сохранениеп сериализации
        serializer.save(card=Card.objects.get(user=self.request.user, status=True))


# class OrderViews(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


class OrderViews(APIView):
    """Делаем заказ"""
    def get_add_cart(self):
        cart = Card.objects.get(user=self.request.user, status=True)
        cart.status = False
        cart.save()
        Card.objects.create(user=self.request.user)
        return cart

    def post(self, request, *args, **kwargs):
        self.order_create(self.get_add_cart())
        return Response(status=status.HTTP_201_CREATED)

    def order_create(self, cart):
        Order.objects.create(card=cart)


class OrderListViews(generics.ListAPIView):
    """все заказы одного пользывателя"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderListSerializer

    def get_queryset(self):
        return Order.objects.filter(card__user=self.request.user)


class CartChange(generics.UpdateAPIView):
    """изменяет количество товара в корзине"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangeOrderSerializer

    def get_queryset(self):
        return CardItem.objects.filter(card__user=self.request.user, card__status=True)


class DeleteProduct(generics.DestroyAPIView):
    """удаляем заказ"""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CardItem.objects.filter(card__user=self.request.user, card__status=True)


class AddComment(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddCommentSerializers

    def perform_create(self, serializer):  # переопредиляем сохранениеп сериализации
        serializer.save(user=self.request.user)

class CommentChange(generics.UpdateAPIView):
    """изменить товар"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangeCommentSerializers

    def perform_create(self, serializer):  # переопредиляем сохранениеп сериализации
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)


class CommentDelete(generics.DestroyAPIView):
    """удалить товар"""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)
