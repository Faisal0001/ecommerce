from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/register/', include('rest_auth.registration.urls')),
    path('products/', include('products.urls'), name='prdoucts_api'),
    path('blogs/', include('blogs.urls'), name='blogs_api')
    
]
