from itertools import product
import profile
from sre_constants import AT_END_STRING
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import *
from .models import *
from .forms import *
from shop.models import ProductModel
from users.models import ProfileModel
from django.db.models import Sum


class CheckoutView(CreateView):
    template_name = 'checkout.html'
    form_class = CheckoutForm
    success_url = 'order/history/'

    # def dispatch(self, request, *args, **kwargs):
    #     if len(request.session['cart', []]) == 0:
    #         return redirect(render('pages:home'))

    #     return super(CheckoutView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['products'] = ProductModel.get_cart_objects(self.request)
        
        if hasattr(self.request.user, 'profiles'):
            context['profile'] = self.request.user.profiles

        return context

    def form_valid(self, form):
        products = ProductModel.get_cart_objects(self.request)
        total_price = products.aggregate(Sum('real_price')).get('real_price__sum', '')
        
        order = form.save(commit=True)
        

        if self.request.user.is_authenticated:
            order.user = self.request.user.id
        order.total_price = total_price
        order.products.set(products)
        order.save()

        self.request.session.get('cart', [])

        return super().form_valid(form)

class OrderHistoryView(ListView):
    template_name = 'order_history.html'


    def get_queryset(self):
        
        return OrderHistoryModel.objects.filter(user=self.request.user.id)