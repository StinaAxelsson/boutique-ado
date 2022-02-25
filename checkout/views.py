from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ f """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KWz8fKxesD1Tm7OtlyDyG9VAy4Yh5xyGOZw9B19Vf5KotzHajixqCPxYyvBeDpOwEo36JlBA8HZomerhH7Zsghd00XZ18xymT',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)