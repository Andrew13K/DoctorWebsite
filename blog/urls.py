from django.urls import path
from .import views
from .views import BlogView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),

]