from django.urls import path
from .views import GetNearByShops, GetShopByDistance

urlpatterns = [
    path('all/shops/', GetNearByShops.as_view()),
    path('shops/near/me/', GetShopByDistance.as_view()),
]
