from django.db.models import Min, Max
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProductModel, productTagModel, CategoryModel, ColorModel, SizeModel, BrandModel

class ShopView(ListView):
    template_name = 'shop.html'
    paginate_by = 2

    def get_queryset(self):
        qs = ProductModel.objects.all().order_by('-id')

        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(title__icontains=search)

        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category=cat)

        tag = self.request.GET.get('tag')

        if tag:
            qs = qs.filter(tags=tag)

        size = self.request.GET.get('size')
        if size:
            qs = qs.filter(sizes=size)

        color = self.request.GET.get('color')
        if color:
            qs = qs.filter(colors=color)

        brand = self.request.GET.get('brand')
        if brand:
            qs = qs.filter(brand_id=brand)

        sort = self.request.GET.get('sort')
        if sort == 'price':
            qs = qs.order_by('price')
        elif sort == '-Price':
            qs = qs.order_by('-price')
        elif sort == 'sale':
            qs = qs.order_by('sale')
        
        price = self.request.GET.get('price')
        if price:
            min, max = price.split(';') # ['150', '325'] min >= real_price and max <= real_price
            qs = qs.filter(real_price__gte=min, real_price__lte=max)
        return qs

    def get_context_data(self, **kwargs):
        
        data = super().get_context_data()
        data['categories'] = CategoryModel.objects.all()
        data['tags'] = productTagModel.objects.all()
        data['sizes'] = SizeModel.objects.all()
        data['brands'] = BrandModel.objects.all()
        data['colors'] = ColorModel.objects.all()
        data['min_price'], data['max_price'] = ProductModel.objects.aggregate(Min('real_price'), Max('real_price')).values()


        return data


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'shop-details.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['products'] = ProductModel.objects.all().exclude(id=self.object.pk)[:4]
        return data
