from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

products_router = routers.NestedSimpleRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')


# URLConf
urlpatterns = router.urls + products_router.urls