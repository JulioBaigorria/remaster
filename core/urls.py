"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from apps.products import views as pviews
from apps.logistic import views as lviews
from rest_framework.documentation import include_docs_urls
from apps.users.views import LogOutView, LogOutAllView
from rest_framework.schemas import get_schema_view
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()

router.register(r'logistic/hr', lviews.HRViewSet),
router.register(r'products/active', pviews.ActiveIngredientViewSet),
router.register(r'products', pviews.ProductsViewSet),

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/logout/', LogOutView.as_view(), name='logout'),
    path('api/logout/all/', LogOutAllView.as_view(), name='logout_all'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Remaster')),
    path('', get_schema_view(
        title='Remaster',
        description='Web API REST Service',
        version='0.0.1'
    ), name='openapi-schema'),
]
