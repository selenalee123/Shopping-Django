from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views 

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

# hello
urlpatterns = router.urls