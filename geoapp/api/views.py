from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import fromstr
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .serializers import ShopSerializer
from geoapp.models import Shop

class GetNearByShops(generics.ListAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

    def get(self, request):
        qs = Shop.objects.all()
        serializer = ShopSerializer(data=qs, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetShopByDistance(APIView):
    serializer_class = ShopSerializer
    
    def get(self, request, *args, **kwargs):
        try:
            longitude = float(request.query_params.get('longitude'))
            latitude = float(request.query_params.get('latitude'))
            user_location = Point(longitude, latitude, srid=4326)
            # print(user_location)
            queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:3]
            serializer = ShopSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_204_NO_CONTENT)
