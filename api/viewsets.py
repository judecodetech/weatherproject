from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from api import serializers

from weatherapp import models


class WeatherForecastViewSet(viewsets.ReadOnlyModelViewSet, APIView):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = models.WeatherForecast.objects.all()
    serializer_class = serializers.WeatherForecastSerializer 
    
    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)   
