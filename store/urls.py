from django.contrib import admin
from django.urls import path, include
from . import views 

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

# hello
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail), #let the interger only
    path('collections/', views.collection_list),
    path('collections/<int:pk>/', views.collection_detail,name='collection-detail'), #let the interger only
]