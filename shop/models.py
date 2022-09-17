from django.db import models
from django.utils.translation import gettext_lazy as tr
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from decimal import *
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.db.models import Sum

UserModel = get_user_model()

class CategoryModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=tr('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class BrandModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=tr('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

class SizeModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=tr('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'

class ColorModel(models.Model):
    code = models.CharField(max_length=60, verbose_name=tr('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))
        
    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'



class ProductTagModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=tr('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tag'



class ProductModel(models.Model):
    title = models.CharField(max_length=60, verbose_name=tr('title'))
    short_description = models.CharField(max_length=255, verbose_name=tr('short description'))
    long_description = RichTextUploadingField()
    price = models.FloatField(verbose_name=tr('price'))
    real_price = models.FloatField(verbose_name=tr('real price'), default=0)
    sale = models.BooleanField(verbose_name=tr('sale'), default=False)
    discount = models.PositiveSmallIntegerField(default=0, verbose_name=tr('discount'))
    main_image = models.ImageField(upload_to='products/', verbose_name=tr('main image'))
    category = models.ForeignKey(
        CategoryModel, 
        on_delete=models.RESTRICT, 
        related_name='products', 
        verbose_name=tr('category')
    )
    tags = models.ManyToManyField(
        ProductTagModel, 
        related_name='Products', 
        verbose_name=tr('tags'),
    )
    sizes = models.ManyToManyField(
        SizeModel, 
        related_name='Products', 
        verbose_name=tr('sizes'),
    )
    colors = models.ManyToManyField(
        ColorModel, 
        related_name='Products', 
        verbose_name=tr('colors'),
    )
    brand = models.ForeignKey(
        BrandModel, on_delete=models.RESTRICT, 
        related_name='Products', 
        verbose_name=tr('brands'),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))


    
    def is_discount(self):
        return bool(self.discount)

    def new(self):
        return (timezone.now() - self.created_at).days <= 5

    @staticmethod
    def get_cart_info(request):
        cart = request.session.get('cart', [])
        if not cart:
            return 0, 0.0
        return len(cart), ProductModel.objects.filter(id__in=cart).aggregate(Sum('real_price'))['real_price__sum']


    @staticmethod
    def get_cart_objects(request):
        cart = request.session.get('cart', [])
        if not cart:
            return None
        return ProductModel.objects.filter(id__in=cart)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class WishlistModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='wishlists', verbose_name=tr('user'))
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name=tr('product'))

    @staticmethod
    def create_or_delete(user, product):
        try:
            return WishlistModel.objects.create(user=user, product=product)
        except IntegrityError:
            return WishlistModel.objects.get(user=user, product=product).delete()

    def __str__(self):
        return f"{self.user.get_full_name()} | {self.product.title}"

    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'
        unique_together = 'user', 'product',


