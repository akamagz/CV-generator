from django.contrib import admin
from django.urls import path
from pdf import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.forms, name='forms'),
    path("cv/<int:id>/", views.cv, name='cv'),
    path("list/", views.list, name='list'),
]
