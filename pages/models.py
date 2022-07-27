from django.db import models
from django.utils.translation import gettext_lazy as tr


class ContactModel(models.Model):
    name = models.CharField(max_length=32, verbose_name=tr('name'))
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = tr('contact')
        verbose_name_plural = tr('contacts')


class BannerModel(models.Model):
    collection = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/', verbose_name=tr('image'))
    # category = models.ForeignKey()
    is_active = models.BooleanField(default=False, blank=True, verbose_name=tr('is_active'))
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = tr('banner')
        verbose_name_plural = tr('banners')

















