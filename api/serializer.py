from rest_framework import serializers

from store.models import Product, Customer, Order
from user.models import Profile


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "category", "quantity"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["name", "phone", "address"]


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(required=True)

    class Meta:
        model = Order
        fields = ["customer", "product", "order_quantity", "price", "total"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["product"] = ProductSerializer(instance.product).data.get("name")
        return rep

    def create(self, validated_data):

        #################  Creating and Saving Customer  #######################

        customer_data = validated_data.pop("customer")
        customer = CustomerSerializer.create(
            CustomerSerializer(), validated_data=customer_data
        )

        ################  Creating Current User Object  #######################

        request = self.context["request"]
        user = request.user

        ###############  Updating Product Quantity when Ordered  #############

        remaining_quantity = (
            validated_data["product"].quantity - validated_data["order_quantity"]
        )
        Product.objects.filter(id=validated_data["product"].id).update(
            quantity=remaining_quantity
        )

        ################# Calculating Total Bill Amount  ##################

        total = validated_data["price"] * validated_data["order_quantity"]

        ##############  Saving Order with staff object  #####################

        obj = Order.objects.create(
            customer=customer, staff=user, total=total, **validated_data
        )
        return obj


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["staff", "phone", "image", "address"]
