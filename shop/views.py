from django.shortcuts import render, get_object_or_404
from .models import Make, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage



def prod_list(request, make_id=None):
    # Fetch all Make objects from the database
    makes = Make.objects.all()  # This gets all makes from the database
    
    # Fetch products based on the selected make
    if make_id:
        make = get_object_or_404(Make, id=make_id)
        products = Product.objects.filter(make=make)  # Adjust based on how you store make in the product model
    else:
        products = Product.objects.all()  # Fetch all products if no make is selected
    
    # Setup pagination
    paginator = Paginator(products, 6)  # 6 products per page
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    # Pass makes and products to the template
    return render(request, 'shop/category.html', {'makes': makes, 'prods': products})
