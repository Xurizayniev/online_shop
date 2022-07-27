from django.db import models
from django.utils.translation import gettext_lazy as tr
from ckeditor_uploader.fields import RichTextUploadingField



class AutherModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=tr('ful name'))
    image = models.ImageField(upload_to='auther_images', verbose_name=tr('image'))

    def __str__(self):
        return self.full_name


    class Meta:
        verbose_name = tr('Auther')
        verbose_name_plural = tr('Authers')


class PostTagModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=tr('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created at'))
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = tr('tag')
        verbose_name_plural = tr('tags')



class PostModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=tr('title'))
    body = RichTextUploadingField(verbose_name=tr('body'))
    main_image = models.ImageField(upload_to='main_images/', verbose_name=tr('main image'))
    banner = models.ImageField(upload_to='post_banners/', verbose_name=tr('banner'))
    auther = models.ForeignKey(AutherModel, related_name='posts', on_delete=models.RESTRICT)
    tag = models.ManyToManyField(PostTagModel, related_name='posts', verbose_name=tr('tag'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created at'))


    def __str__(self):
        return f"{self.title[:100]}..."


    class Meta:
        verbose_name = tr('Post')
        verbose_name_plural = tr('posts')

class CommentModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=tr('name'))
    email = models.EmailField(verbose_name=tr('email'))
    phone = models.CharField(max_length=13, verbose_name=tr('phone'))
    comment = models.TextField(verbose_name=tr('comment'))
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments', verbose_name=tr('post'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created at'))

    def __str__(self):
        return f"{self.name}\n{self.email}\n{self.phone}\n{self.comment}"

    class Meta:    
        verbose_name = tr('comment')
        verbose_name_plural = tr('comments')
