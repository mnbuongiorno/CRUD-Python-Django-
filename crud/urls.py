from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='inicio'),
    path('products', views.consult, name='consult'),
    path('products/save_products', views.save_products, name="save_products"),
    path('products/delete/<int:id>', views.delete, name="delete"),
    path('products/details/<int:id>', views.details, name="details"),
    path('products/edit', views.edit, name="edit"),
]
