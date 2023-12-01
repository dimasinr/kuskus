"""
URL configuration for kuskus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from thread import views as thread
from users import views as user

urlpatterns = (
    [
        path('admin/', admin.site.urls),
        path('auth/login/', user.index_login, name='login'),
        path('auth/register/', user.index_register, name='register'),
        path('profile/', user.index_profile, name='profile'),
        path('auth/logout/', user.logout, name='logout'),
        path('', thread.homepage, name='home'),
        path('thread/<int:thread_id>/', thread.detail_thread, name='detail_thread'),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
