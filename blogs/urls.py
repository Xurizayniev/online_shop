from django.urls import path
from .views import PostListView, PostDetailView, CommentCreatView

app_name = 'blogs'

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/post', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', CommentCreatView.as_view(), name='comment')
]

