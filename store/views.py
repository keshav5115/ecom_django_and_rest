from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


from .models import Customer, Product, Order
from .forms import ProductForm, CustomerForm, OrderForm


def nav_items():
    orders_count = Order.objects.all().count()
    products_count = Product.objects.all().count()
    workers_count = User.objects.all().count()
    customers_count = Customer.objects.count()
    data = {
        "orders_count": orders_count,
        "workers_count": workers_count,
        "products_count": products_count,
        "customers_count": customers_count,
    }
    return data


@login_required
def index(request):
    orders = Order.objects.select_related("customer", "product").filter(
        staff=request.user
    )
    if request.method == "POST":
        form = OrderForm(request.POST)
        form1 = CustomerForm(request.POST)
        if form.is_valid() and form1.is_valid():
            form1.save()
            instance = form.save(commit=False)
            instance.customer = Customer.objects.all().latest("id")
            instance.staff = request.user
            instance.total = instance.price * instance.order_quantity

            # Updating Product quantity

            instance.product.quantity -= form.cleaned_data.get("order_quantity")
            product = Product.objects.filter(id=instance.product.pk)
            product.update(quantity=instance.product.quantity)

            instance.save()

            return redirect("store-index")
    else:
        form = OrderForm()
        form1 = CustomerForm()
    context = {
        "orders": orders,
        "form": form,
        "form1": form1,
    }
    context.update(nav_items())
    return render(request, "index.html", context)


@login_required
def staff(request):
    workers = User.objects.all()
    context = {
        "workers": workers,
    }
    context.update(nav_items())
    return render(request, "staff.html", context)


@login_required
def staff_detail(request, pk):
    worker = User.objects.get(id=pk)
    context = {"worker": worker}
    context.update(nav_items())
    return render(request, "staff_detail.html", context)


@login_required
def product(request):
    items = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get("name")
            messages.success(request, f"{product_name} added successfully")
            return redirect("store-product")
    else:
        form = ProductForm()

    context = {
        "items": items,
        "form": form,
    }
    context.update(nav_items())
    return render(request, "product.html", context)


@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("store-product")
    return render(request, "product_delete.html")


@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("store-product")

    else:
        form = ProductForm(instance=item)
    context = {
        "form": form,
    }
    context.update(nav_items())
    return render(request, "product_update.html", context)


@login_required
def customer(request):
    customers = Customer.objects.all()
    context = {"customers": customers}
    context.update(nav_items())
    return render(request, "customer.html", context)


@login_required
def customer_update(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("store-customer")
    else:
        form = CustomerForm(instance=customer)

    context = {"form": form}
    return render(request, "customer_update.html", context)


@login_required
def customer_delete(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect("store-customer")
    return render(request, "customer_delete.html")


@login_required
def order(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    context.update(nav_items())
    return render(request, "order.html", context)
