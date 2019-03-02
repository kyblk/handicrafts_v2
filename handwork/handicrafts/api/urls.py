from rest_framework import routers

from .views import MainSliderViewSet, CatalogViewSet, ProductListViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()

router.register(r'sliders', MainSliderViewSet)
router.register(r'catalog/(?P<slug>[\w-]+)', ProductListViewSet, base_name="catalog-detail")
router.register(r'catalog', CatalogViewSet)

# URLs настраиваются автоматически роутером
urlpatterns = router.urls
