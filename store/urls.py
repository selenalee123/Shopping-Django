from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from . import views 

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router,'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

# hello
urlpatterns = router.urls + products_router.urls