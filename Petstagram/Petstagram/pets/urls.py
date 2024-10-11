"""
URL configuration for Petstagram project.

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
from django.urls import path, include
from Petstagram.pets import views
urlpatterns = [
    path('add/', views.pet_add_page, name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>', include([
        path('', views.pet_detail_page, name='detail-pet'),
        path('edit/', views.pet_edit_page, name='edit-pet'),
        path('delete/', views.pet_delete_page, name='delete-pet'),

    ]))
]