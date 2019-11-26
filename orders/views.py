from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cartapp.views import cartview
from cartapp.models import cart


def order_create(request):
    cart = cartview(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                cart.objects.create(
                    order=order,
                    price=item['unitprice'],
                    quantity=item['units']
                )
            cart.clear()
        return render(request, 'created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'create.html', {'form': form})