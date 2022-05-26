from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'', views.ClientViewSet, basename='clients')

urlpatterns = router.urls
