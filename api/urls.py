from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProductModelViewSet, OrderModelViewSet, UserModelViewSet

router = DefaultRouter()
router.register("product_api", ProductModelViewSet, basename="product_api")
router.register("order_api", OrderModelViewSet, basename="order_api")
router.register("user_api", UserModelViewSet, basename="user_api")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls")),
]
