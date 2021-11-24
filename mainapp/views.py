from django.shortcuts import render
import json
import os
from mainapp.models import ProductCategory, Product

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'geekshop - каталог',
        # 'products': [
        #    {'name': 'Худи черного цвета с монограммами adidas Originals',
        #     'price': '6 090,00 руб.',
        #     'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
        #     'pic': 'vendor/img/products/Adidas-hoodie.png'},
        #    {'name': 'Синяя куртка The North Face',
        #     'price': '23 725,00 руб.',
        #     'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
        #     'pic': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
        #    {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
        #     'price': '3 390,00 руб.',
        #     'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
        #     'pic': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
        #   {'name': 'Черный рюкзак Nike Heritage',
        #     'price': '2 340,00 руб.',
        #     'description': 'Плотная ткань. Легкий материал.',
        #     'pic': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
        #    {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
        #     'price': '13 590,00 руб.',
        #     'description': 'Гладкий кожаный верх. Натуральный материал.',
        #     'pic': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
        #    {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
        #     'price': '2 890,00 руб.',
        #     'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
        #    'pic': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
        # ],
        'categories': ProductCategory.objects.all(),
    }
    # context['products'] = json.load(open(file_path, encoding='utf-8'))
    context['products'] = Product.objects.all()
    return render(request, 'mainapp/products.html', context)

