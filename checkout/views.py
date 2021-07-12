from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    # It will prevent from manually accessing the URL by typing /checkout
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J3fnNDq6Ek3HX07Qsxg6cT9g8vIDag5HE6mgCtYkH9KJ2RpzgKcXTXhSCWA6UPbmvKbKnbf1NGDkGtiUgpa4JX300Qr3IPmuH',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
