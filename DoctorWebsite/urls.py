from django.contrib import admin
from django.urls import path, include

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('news/', include('blog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]