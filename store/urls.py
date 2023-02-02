from django.urls import path
from . import views

urlpatterns = [
    path("store/", views.index, name="store-index"),
    path("staff/", views.staff, name="store-staff"),
    path("staff/detail/<int:pk>/", views.staff_detail, name="store-staff-detail"),
    path("product/", views.product, name="store-product"),
    path("product/delete/<int:pk>/", views.product_delete, name="store-product-delete"),
    path("product/update/<int:pk>/", views.product_update, name="store-product-update"),
    path("customer/", views.customer, name="store-customer"),
    path(
        "customer/update/<int:pk>/", views.customer_update, name="store-customer-update"
    ),
    path(
        "customer/delete/<int:pk>/", views.customer_delete, name="store-customer-delete"
    ),
    path("order/", views.order, name="store-order"),
]
