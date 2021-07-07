from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    # initialized to zero
    bag_items = []
    total = 0
    product_count = 0

    # if total < 50
    if total < settings.FREE_DELIVERY_THRESHOLD:
        # total*10%=delivery
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        # how much left to got free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
