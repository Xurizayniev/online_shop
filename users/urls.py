from django.urls import path
from .views import *

app_name='user'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', logout_view, name='logout'),
    path('login/', loginview, name='login'),
    path('registration/', user_registration, name='registration'),

]
