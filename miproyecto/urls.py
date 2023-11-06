from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('perfiles.urls')),
    path('',include('blog.urls')),
]

