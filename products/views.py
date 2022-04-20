""" Products view """
from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, get_list_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import Http404
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm

# Create your views here.


def all_products(request):
    """ A view to return products, sorting, and search queries """

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

            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('products'))

            name_q = Q(name__icontains=query)
            description_q = Q(description__icontains=query)

            queries = name_q | description_q
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return a product detail page """

    product = get_object_or_404(Product, pk=product_id)
    no_reviews_list = False
    try:
        reviews = get_list_or_404(Review, product=product)

        for review in reviews:
            if request.user == review.user:
                review_exists = True
                break
    except Http404:
        no_reviews_list = True
    review_exists = False

    form = ReviewForm(instance=product)

    template = 'products/product_detail.html'
    if no_reviews_list:
        context = {
            'product': product,
            'form': form,
            'review_exists': review_exists,
            'no_reviews_list': no_reviews_list
        }
    else:
        context = {
            'product': product,
            'form': form,
            'reviews': reviews,
            'review_exists': review_exists,
            'no_reviews_list': no_reviews_list
        }

    return render(request, template, context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ A view to add a product review """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':  # Form to add review
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review_data = form.save(commit=False)
            review_data.product = product
            review_data.user = request.user
            review_data.review = request.POST['review']
            review_data.save()
            messages.success(request, 'Successfully reviewed product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to review product. \
                Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=product)

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def edit_review(request, product_id, review_id):
    """ A view to edit a product review """

    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)
    reviews = get_list_or_404(Review, product=product)
    review_exists = False

    for review in reviews:
        if request.user == review.user:
            review_exists = True
            break

    if request.method == 'POST':  # Form to edit review
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update review. \
                Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)

    template = 'products/edit_review.html'
    context = {
        'product': product,
        'form': form,
        'review': review,
        'reviews': reviews,
        'review_exists': review_exists
    }

    return render(request, template, context)


@login_required
def delete_review(request, product_id, review_id):
    """ A view to return a product detail page """

    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)
    if request.user == review.user:
        review.delete()
    messages.success(request, 'Successfully removed review!')

    return redirect(reverse('product_detail', args=[product.id]))
