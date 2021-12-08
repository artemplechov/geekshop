from django.shortcuts import render
import json
import os

from django.views.generic import DetailView

from mainapp.models import ProductCategory, Product

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=None):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'Geekshop | Каталог',
    }

    if id_category:
        context['products'] = Product.objects.filter(category_id=id_category)
    else:
        context['products'] = Product.objects.all()

    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'


    def get_context_data(self, **kwargs):
        context = super(ProductDetail,self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
