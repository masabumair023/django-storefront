from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

# URLConf
urlpatterns = router.urls

# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:id>/', views.ProductDetails.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     path('collections/<int:id>/', views.CollectionDetails.as_view()),
# ]