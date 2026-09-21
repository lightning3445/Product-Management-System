"""
URL configuration for product_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
# This imports Django's settings.
from django.conf.urls.static import static
# static() is a Django helper that creates 
# URL patterns for serving files from a folder.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("product.urls")),
]


urlpatterns+=static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
    
)

# static() is a Django function that 
# creates URL patterns for serving files

# settings.MEDIA_URL,
#     # This means uploaded files will be 
#     # accessed through URLs starting with:/media/
# document_root=settings.MEDIA_ROOT
#     # This tells Django:
#     # "The actual files are stored inside 
#     # the media folder."