from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    Renders products.html and displays
    all products on website. Search and 
    filter option will also be included.
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                # sort by name rather than id, using double under score to
                # gain access into related object model
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # splitting into list after commas and filter list who's 
        # category name is in the list
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # double underscore for django's built in search
            products = products.filter(category__name__in=categories)
            # category objects created from search used to display them products.html
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "No search criteria recognized, please try again.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    chosen_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_word': query,
        'chosen_categories': categories,
        'chosen_sorting': chosen_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    Renders product_detail.html to display
    all info regarding each specific product
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


# login decorator used so if user is not logged in, redirect to log in page.
@login_required
def add_product(request):
    """Add a product to the store"""
    # only superuser can access this function
    if not request.user.is_superuser:
        messages.error(request, 'Sorry but you do not have access to this task.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form = product_form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product_form.id]))
        else:
            messages.error(request, 'Failed to add product. Please try again.')
    else:
        product_form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
    }

    return render(request, template, context)


# login decorator used so if user is not logged in, redirect to log in page.
@login_required
def update_product(request, product_id):
    """Update a product in the store"""
    # only superuser can access this function
    if not request.user.is_superuser:
        messages.error(request, 'Sorry but you do not have access to this task.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        product_form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/update_product.html'
    context = {
        'product_form': product_form,
        'product': product,
    }

    return render(request, template, context)


# login decorator used so if user is not logged in, redirect to log in page.
@login_required
def delete_product(request, product_id):
    """Delete a product in the store"""
    # only superuser can access this function
    if not request.user.is_superuser:
        messages.error(request, 'Sorry but you do not have access to this task.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        product.delete()
        messages.success(request, 'Product successfully deleted!')
        return redirect('products')
    context = {
        'product': product
    }

    return render(request, 'products/delete_product.html', context)
