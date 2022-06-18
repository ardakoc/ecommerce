from django.shortcuts import render

from store.models import Order, Product

# Create your views here.

def store(request):
  products = Product.objects.all()
  context = {'products': products}
  return render(request, 'store/store.html', context)


def cart(request):
  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
  else:
    # create empty cart for now for unauthenticated users
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    items = []

  context = {'order': order, 'items': items}
  return render(request, 'store/cart.html', context)


def checkout(request):
  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
  else:
    # create empty cart for now for unauthenticated users
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    items = []

  context = {'order': order, 'items': items}
  return render(request, 'store/checkout.html', context)