from django.urls import include, path
from rest_framework import routers
from .views import *
from django.contrib import admin

router = routers.DefaultRouter()
# router.register(r'products', )

urlpatterns = [
    path('product/<int:pk>/', ViewUpdateDeleteProducts.as_view(), name='view_products'),
    path('products_list/', ListCreateProducts.as_view(), name='list_products'),
    path('cart/', ViewDeleteCart.as_view(), name='cart'),
    path('insert_cart/', InsertToCart.as_view(), name='insert_cart'),
    path('container/', ViewCreateContainer.as_view(), name='container'),
    path('reviews/<str:product>/', ListCreateReviews.as_view(), name='reviews'),
    path('ratings/<str:product>/<str:userID>/<int:rate>/', ViewUpdateRatings.as_view(), name='ratings'),
    path('average_rating/<str:product>/', ListRatings.as_view(), name='rate'),
    path('coupon/', Coupons.as_view(), name='coupon'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('search/', SearchProducts.as_view(), name='search'),
]
