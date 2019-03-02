from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class CatalogView(TemplateView):
    template_name = "catalog.html"


class ProductListView(TemplateView):
    template_name = "product_list.html"


class ProductDetailView(TemplateView):
    template_name = "product_detail.html"


# Create your views here.
