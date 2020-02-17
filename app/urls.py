
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('category', CategoryListView.as_view(), name='category'),
    path('add-item/', AddCartItemViews.as_view()),
    path('cart/', FilterCardListView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),
    path('category/<slug:slug>/', FilterCategoryListView.as_view()),
    path('order/', OrderViews.as_view()),
    path('orderlist/', OrderListViews.as_view()),
    path('cart-change/<int:pk>/', CartChange.as_view()),
    path('delete/<int:pk>/', DeleteProduct.as_view()),
    path('add-comment', AddComment.as_view()),
    path('comment-change/<int:pk>/', CommentChange.as_view()),
    path('comment-delete/<int:pk>/', CommentDelete.as_view()),
]