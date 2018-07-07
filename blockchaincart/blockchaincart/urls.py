from django.conf.urls import url
from rest_framework import routers
from django.contrib import admin
from django.urls import include, path
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
router = routers.DefaultRouter()
urlpatterns = [
    # url('', include(router.urls)),
    path('', include('shop.urls')),
    path('admin/', admin.site.urls),
    # Examples:
    # url(r'^$', 'blockchaincart.views.home', name='home'),
    # url(r'^blockchaincart/', include('blockchaincart.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url('admin/', include(admin.site.urls)),
]
