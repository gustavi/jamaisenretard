"""jamaisenretard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from jamaisenretard.booking.views import PersonViewSet, ClientAccountViewSet, HotelBookingViewSet, FlyBookingViewSet, \
    BookingViewSet, IndexView
from jamaisenretard.member.views import UserViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'client-accounts', ClientAccountViewSet)
router.register(r'hotel-bookings', HotelBookingViewSet)
router.register(r'fly-bookings', FlyBookingViewSet)
router.register(r'bookings', BookingViewSet)


schema_view = get_swagger_view(title='JamaisEnRetard API')


urlpatterns = [
    path('', IndexView.as_view(), name='home'),

    path('api/v1/', include(router.urls)),
    path('api/doc/v1/', schema_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]
