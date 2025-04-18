"""
URL configuration for template project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from training_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.contact_list, name = "contact_list"),
    path('add_contact', views.add_contact),
    path('about_contact<int:contact_id>', views.about_contact, name='about_contact'),
    path('edit_contact', views.edit_contact),
    path('edit_contact<int:pk>', views.edit_contact),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
