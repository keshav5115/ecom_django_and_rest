from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializer import ProductSerializer, OrderSerializer, UserSerializer
from store.models import Product, Order
from user.models import Profile


class ProductModelViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]


class OrderModelViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    ############    Overriding get_queryset() method for user based query ##############

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            queryset = Order.objects.all()
        else:
            queryset = Order.objects.filter(staff=user)

        return queryset


class UserModelViewSet(ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
