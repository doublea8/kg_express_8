from django.http import Http404
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
        product = Product.objects.get(id=pk)
        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     data = form.cleaned_data
        cart.add(
            product=product
            # quantity=data['quantity'],
            # update_quantity=data['update']
        )

        return redirect('cart_detail')


class CartDetailView(View):

    def get(self, request):
        return render(self.request, 'cart.html')


class RemoveCartView(View):

    def get(self, request, pk):
        cart = Cart(request)
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404
        cart.remove(product)
        return redirect('cart_detail')


class ClearCartView(View):

    def get(self, request):
        cart = Cart(request)
        cart.clear()
        return redirect("cart_detail")


from django.http import JsonResponse
def add_cart_product(request, pk):
    if request.method == 'POST':
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404
        cart = Cart(request)
        cart.add(
            product=product
        )
        return JsonResponse({'message': 'Ok'}, status=200)
    return JsonResponse({'message': 'Bad Request'}, status=200)
