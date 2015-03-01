from django.shortcuts import render
from django.contrib.auth.models import User
from gps.models import GpsNode, GpsNodeMetrics
from rest_framework import generics, viewsets, permissions

from gps.serializers import UserSerializer, GpsNodeSerializer, GpsNodeMetricSerializer

# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class GpsNodeViewSet(viewsets.ModelViewSet):
    queryset = GpsNode.objects.all()
    serializer_class = GpsNodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        print "Viewset: GpsNode.perform_create %r" %repr(self.request)
        serializer.save(user=self.request.user)

class GpsNodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GpsNode.objects.all()
    serializer_class = GpsNodeSerializer
