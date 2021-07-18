from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_basket(request):
    """ A view that loads the basket contents page """

    return render(request, 'basket/basket.html')


# function to take both the request and add the product id to the basket
def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    # get the quantity from the the and url to redirect the user to
    product = get_object_or_404(Product, pk=item_id)
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    """ session created till the browser is closed to keep the user
    shopping or if they would like to come back to it"""
    basket = request.session.get('basket', {})

    # adding the product and quantity in the basket, and if the product is already there, add the quantity to the basket
    if item_id in list(basket.keys()):
        messages.error(
            request, f'Item is already in the basket {product.name}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'product has been add {product.name}')

    # overwriting the variable in the session with the updated version of the basket
    request.session['basket'] = basket
    return redirect(redirect_url)


# function to remove the product from the basket
def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    # try block to catch any expections that might happen with a server 500 error
    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id)

        request.session['basket'] = basket
        messages.success(request, f'product has been removed {product.name}')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
