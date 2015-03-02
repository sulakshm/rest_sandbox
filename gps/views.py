from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from gps.models import GpsNode, GpsNodeMetrics
from gps.permissions import IsOwnerOrNone, IsOwnerOrReadOnly
from rest_framework import generics, viewsets, permissions

from gps.serializers import UserSerializer, GpsNodeSerializer, GpsNodeMetricSerializer

# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (IsOwnerOrReadOnly,)

    def update(self, request, pk=None):
        u=get_object_or_404(User, pk)
        if request.user.id != u.id:
            raise Http404('No permission to modify entry'
        return super(UserViewSet, self).update(request, pk)

class GpsNodeViewSet(viewsets.ModelViewSet):
    #queryset = GpsNode.objects.all()
    serializer_class = GpsNodeSerializer
    permission_classes = (IsOwnerOrNone,)

   def get_queryset(self):
       return self.request.user.nodes.all()

    def perform_create(self, serializer):
        print "Viewset: GpsNode.perform_create %r" %repr(self.request)
        serializer.save(user=self.request.user)

class GpsNodeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrNone,)
    queryset = GpsNode.objects.all()
    serializer_class = GpsNodeSerializer
