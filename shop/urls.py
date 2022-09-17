from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', ShopView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product/<int:pk>/wishlist/', wishlist_View, name='wishlist'),
    path('wishlists/', WishtlistView.as_view(), name='all_wishlist'),
    path('add_cart/<int:id>/', update_cart_view, name='cart'),
    path('shopping_cart/', ShopingCartView.as_view(), name='shop_cart'),
]

