from ast import Or
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  #new

urlpatterns = [
    path("", views.index, name='app'),
    path("landDetails", views.landDetails, name='details'), # added later
    path("add_post", views.add_post, name='add'), # added later
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact')

]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)