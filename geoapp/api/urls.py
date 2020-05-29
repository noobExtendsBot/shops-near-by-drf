from django.urls import path
from .views import GetAllShops, GetNearByShops

urlpatterns = [
    path('all/shops/', GetAllShops.as_view()),
    path('shops/near/me/', GetNearByShops.as_view()),
]
