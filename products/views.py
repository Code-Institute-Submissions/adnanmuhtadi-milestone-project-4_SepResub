from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category


# Create your views here.


def all_products(request):
    """ A view to show all the products, including the sorting and searching,
    Context is added to send things back to the template"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # checking if category request.GET exists
    if request.GET:
        if 'sort' in request.GET:
            # allowing sort to also equals sortkey
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                # rename sortkey to lower_name in the event user sorting by name
                sortkey == 'lower_name'
                # annotate the list of products with the new field
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # check if the direction is descending or ascending
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # to sort the products
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            # take the list of results and split in the ','
            categories = request.GET['category'].split(',')
            # using that list, it will filter the products based on the name of the categories
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # checking if request.GET exists and using the search_q parameters
        # if search_q is in request.GET then call it query
        if 'search_q' in request.GET:
            query = request.GET['search_q']
            # Error message appear if query is blank, and then redirects them to products view
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            # setting a variable to Q object where it is searching content using the name or description
            search_results = Q(name__icontains=query) | Q(
                description__icontains=query)
            # pass the results through the filter method
            products = products.filter(search_results)

    sorting_products = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'present_categories': categories,
        'sorting_products': sorting_products,
    }

    return render(request, 'products/products.html', context)

# Product detail view


def product_detail(request, product_id):
    """ A view to show a specific product by take the parameter Product ID, 
    Context is added to send things back to the template"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)