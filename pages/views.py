from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from .forms import *
from blogs.models import PostModel
from .models import BannerModel

class HomePageView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        data = super(HomePageView, self).get_context_data(**kwargs)
        data['post'] = PostModel.objects.order_by('-pk')[:3]
        data['banners'] = BannerModel.objects.filter(is_active=True).order_by('-id')
        return data

class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm


    def get_success_url(self):
        return reverse('pages:contact')