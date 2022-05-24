from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from .forms import CartAddForm
from .cart import Cart
from ..product.models import Product


class AddCartView(View):
    # form_class = CartAddForm

    def get(self, request, pk):
        product_id = self.kwargs.get('pk')
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     data = form.cleaned_data
        cart.add(
            product=product
            # quantity=data['quantity'],
            # update_quantity=data['update']
        )

        return redirect('index')


class CartDetailView(View):

    def get(self, request):
        return render(self.request, 'cart.html')