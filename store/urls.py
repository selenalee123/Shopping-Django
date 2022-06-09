from django.contrib import admin
from django.urls import path, include
from . import views 

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

# hello
urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()), #let the interger only
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(),name='collection-detail'), #let the interger only
]