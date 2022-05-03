from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'logout', views.LogOutView, basename='logout')
router.register(r'logout/all', views.LogOutAllView, basename='logoutall')
router.register(r'', views.UserViewSet, basename='users')

urlpatterns = router.urls
