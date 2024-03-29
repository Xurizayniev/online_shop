from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import ProductModel

@receiver(pre_save, sender=ProductModel)
def get_real_price(sender, instance, *args, **kwargs):
    
    if instance.is_discount():
        instance.real_price = ((100 - instance.discount) / 100) * instance.price
    else:
        instance.real_price = instance.price

@receiver(pre_save, sender=ProductModel)
def set_sale(sender, instance, *args, **kwargs):
    
    if instance.is_discount():
        instance.sale = True
    else:
        instance.sale = False
