from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'active', views.ActiveIngredientViewSet)
router.register(r'', views.ProductsViewSet)

urlpatterns = router.urls
