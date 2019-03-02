from django.conf.urls import url

from .views import IndexView, CatalogView, ProductListView, ProductDetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^catalog/$', CatalogView.as_view(), name='catalog_view'),
    url(r'^catalog/(?P<slug>[\w-]+)/$', ProductListView.as_view(), name='product_list_view'),
    url(r'^catalog/(?P<c_slug>[\w-]+)/product/(?P<p_slug>[\w-]+)/$', ProductDetailView.as_view(),
        name='product_detail_view'),

]