from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Item, Order, OrderItem
from django.views.generic import ListView, DetailView

# Create your views here.

def checkout(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "checkout.html", context)


class HomeView(ListView):
    model = Item
    template_name = 'home.html'


class ProductDetailView(DetailView):
    model = Item
    template_name = 'product.html'
     
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_queryset = Order.objects.filter(user=request.user, ordered=False)
    if order_queryset.exists():
        order = order_queryset[0]
        # Check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:product", slug=slug)