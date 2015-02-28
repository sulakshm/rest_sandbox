from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from gps.models import GpsNode

# Serializers define the API representation.
class GpsNodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GpsNode
        fields = ('ident', 'user', 'created', 'lastActive', 
                           'was_active_recently')

# ViewSets define the view behavior.
class GpsNodeViewSet(viewsets.ModelViewSet):
    queryset = GpsNode.objects.all()
    serializer_class = GpsNodeSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'GpsNodes', GpsNodeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_sandbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
"""
