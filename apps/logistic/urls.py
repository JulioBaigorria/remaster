from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'hr', views.HRViewSet, basename='hr')
router.register(r'drivers/accounts', views.DriverAccountViewSet, basename='accounts')
router.register(r'drivers/vehicles/payloads', views.PayloadViewSet, basename='payloads')
router.register(r'drivers/vehicles/types', views.VehicleTypeViewSet, basename='vehicletypes')
router.register(r'drivers/vehicles', views.VehicleViewSet, basename='vehicles')
router.register(r'drivers', views.DriverViewSet, basename='drivers')

urlpatterns = router.urls
