
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Product, Company, Category, Season, ProductComposition, SizeCloth, SizeShoes
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required


def get_products(request):
    products = Product.objects.all()
    return render(request, 'companies/products.html', {'products': products})



def get_clothing(request):
    products = Product.objects.filter(category__name_category='Одежда')
    return render(request, 'companies/products.html', {'products': products})

def get_shoes(request):
    products = Product.objects.filter(category__name_category='Обувь')
    return render(request, 'companies/products.html', {'products': products})

def get_accessories(request):
    products = Product.objects.filter(category__name_category='Аксессуары')
    return render(request, 'companies/products.html', {'products': products})



def get_pants(request):
    products = Product.objects.filter(name_prod='Брюки')
    return render(request, 'companies/products.html', {'products': products})

def get_jumpers(request):
    products = Product.objects.filter(name_prod='Джемпера')
    return render(request, 'companies/products.html', {'products': products})

def get_jeans(request):
    products = Product.objects.filter(name_prod='Джинсы')
    return render(request, 'companies/products.html', {'products': products})

def get_jackets(request):
    products = Product.objects.filter(name_prod='Куртки')
    return render(request, 'companies/products.html', {'products': products})

def get_coats(request):
    products = Product.objects.filter(name_prod='Пальто')
    return render(request, 'companies/products.html', {'products': products})

def get_shirts(request):
    products = Product.objects.filter(name_prod='Рубашки')
    return render(request, 'companies/products.html', {'products': products})

def get_tshirts(request):
    products = Product.objects.filter(name_prod='Футболки')
    return render(request, 'companies/products.html', {'products': products})

def get_boots(request):
    products = Product.objects.filter(name_prod='Ботинки')
    return render(request, 'companies/products.html', {'products': products})

def get_sneakers(request):
    products = Product.objects.filter(name_prod='Кроссовки')
    return render(request, 'companies/products.html', {'products': products})

def get_moccasins(request):
    products = Product.objects.filter(name_prod='Мокасины')
    return render(request, 'companies/products.html', {'products': products})

def get_list_shoes(request):
    products = Product.objects.filter(name_prod='Туфли')
    return render(request, 'companies/products.html', {'products': products})

def get_ties(request):
    products = Product.objects.filter(name_prod='Галстуки')
    return render(request, 'companies/products.html', {'products': products})

def get_wallets(request):
    products = Product.objects.filter(name_prod='Кошельки')
    return render(request, 'companies/products.html', {'products': products})

def get_belts(request):
    products = Product.objects.filter(name_prod='Ремни')
    return render(request, 'companies/products.html', {'products': products})

def get_bags(request):
    products = Product.objects.filter(name_prod='Сумки')
    return render(request, 'companies/products.html', {'products': products})

def get_scavers(request):
    products = Product.objects.filter(name_prod='Шарфы')
    return render(request, 'companies/products.html', {'products': products})



def get_product_by_id(request, product_id):
    product = Product.objects.get(id=product_id)
    category_list = Category.objects.all()
    season_list = Season.objects.all()
    composition_list = ProductComposition.objects.all()
    size_cloth_list = SizeCloth.objects.all()
    size_shoes_list = SizeShoes.objects.all()
    company_list = Company.objects.all()

    data = {
        'product': product,
        'categories': category_list,
        'seasons': season_list,
        'compositions': composition_list,
        'size_clothes': size_cloth_list,
        'size_shoes': size_shoes_list,
        'companies': company_list,
    }

    return render(request, 'companies/get_product_by_id.html', data)



def update_product(request: HttpRequest, product_id: int):
    """
    Обновляет объект товара с предоставленной информацией из HttpRequest.

    Параметры:
        request (HttpRequest): Объект HTTP-запроса.
        product_id (int): Идентификатор обновляемого товара.

    Возвращает:
        HttpResponseRedirect: Перенаправляет на URL 'get-products' после обновления товара.
    """
    if request.method != 'POST':                      # Проверяет запрос на POST-метод. Если не POST, то возвращает ошибку
        return HttpResponse('Invalid request method')

    product = Product.objects.get(id=product_id)       # Получаем объект товара по ID

                                                       # Получаем "НОВЫЕ" ДАННЫЕ:
    product_name_prod = request.POST.get('name_prod')            # Наименование
    product_article = request.POST.get('article')                # Артикул
    product_description = request.POST.get('description')        # Описание
    product_color = request.POST.get('color')                    # Цвет
    product_price = request.POST.get('price')                    # Цена
    product_product_count = request.POST.get('product_count')    # Количество
    category_id = request.POST.get('category_id')                # Года выпуска get('категорию'),
    season_id = request.POST.get('season_id')                    # Сезон get('сезон'),
    product_composition_id = request.POST.get('product_composition_id')  # Состав get('состав'),
    size_cloth_id = request.POST.get('size_cloth_id')           # Размер одежды get('размер одежды'),
    size_shoes_id = request.POST.get('size_shoes_id')           # Размер обуви get('размер обуви'),
    company_id = request.POST.get('company_id')                 # Производитель get('производитель'),
                                           # Идентификаторы 'КАТЕГОРИИ', 'СЕЗОНА' и т.д. из POST-запроса!!!
                                           # Почему назвали category_id и season_id - из Models.py -> Class Product !!!
                                           # category = models.ForeignKey(Category...)
                                           # season = models.ForeignKey(Season ...)

    category = Category.objects.get(id=category_id)           # Находим КАТЕГОРИЮ по соотв-щим идентификатору
    season = Season.objects.get(id=season_id)                 # Находим CЕЗОН по соотв-щим идентификатору
    product_composition = ProductComposition.objects.get(id=product_composition_id)  # СОСТАВ
    size_cloth = SizeCloth.objects.get(id=size_cloth_id)                             # РАЗМЕР ОДЕЖДЫ
    size_shoes = SizeShoes.objects.get(id=size_shoes_id)                             # РАЗМЕР ОБУВИ
    company = Company.objects.get(id=company_id)                                     # Производителя
                                                                    # т.е. получаем эти объекты по ID

                                              # ОБНОВЛЯЕМ данные товара по заданным полям!
    product.name_prod = product_name_prod
    product.article = product_article
    product.description = product_description
    product.color = product_color
    product.price = product_price
    product.product_count = product_product_count
    product.category = category
    product.season = season
    product.product_composition = product_composition
    product.size_cloth = size_cloth
    product.size_shoes = size_shoes
    product.company = company

    product.save()                             # СОХРАНЯЕМ изменения в БАЗЕ данных

    return HttpResponseRedirect(reverse('get-products')) # После сохранения перенаправляем на страницу со списком товаров!!!

                                                    # reverse - возвращает "ИМЯ" URL, соответствующее указанному адресу.
                                                    # Т.е. reverse('get-products') = '/product/get-products/'


def delete_product(request: HttpRequest, product_id: int):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('get-products'))  # reverse - возвращает URL по 'имени представления'



# """
# Представление для добавления нового автомобиля в автопарк.
# Обрабатывает как GET, так и POST запросы.
# Для GET запросов извлекает список марок и типов автомобилей и рендерит шаблон 'add_product.html' с данными.
# Для POST запросов извлекает детали автомобиля из запроса и сохраняет новый автомобиль
# в базу данных, затем перенаправляется на URL 'get-products'.
# """

@login_required  # декоратор, требующий аутентификации пользователя
# @permission_required('car.p1')  # декоратор, требующий наличия определенных разрешений
def add_product(request):  # Функция принимает параметр request
    if request.method == 'GET':
        category_list = Category.objects.all()               # Если запрос GET, то:
        season_list = Season.objects.all()                   # функция извлекает все данные товара с ForeignKey из БД
        composition_list = ProductComposition.objects.all()
        size_cloth_list = SizeCloth.objects.all()
        size_shoes_list = SizeShoes.objects.all()
        company_list = Company.objects.all()

        data = {                                # таким образом передали в шаблон 6 словарей:
            'categories': category_list,        # ДЛЯ УДОБСТВА заполнения этих полей в шаблоне - делаем их в виде
            'seasons': season_list,             # выпадающего списка - см. models.py !!!
            'compositions': composition_list,
            'size_clothes': size_cloth_list,
            'size_shoes': size_shoes_list,
            'companies': company_list,
        }
        return render(request, 'companies/add_product.html', data)

    # функция render() возвращает шаблон 'add_product.html', где мы заполняем ВСЕ данные для НОВОГО товара
    # см.models.py !!!

    # Если метод запроса равен 'POST', то функция извлекает данные из запроса POST из заполненных полей шаблона
    if request.method == 'POST':
        name_prod = request.POST.get('name_prod')
        article = request.POST.get('article')
        description = request.POST.get('description')
        color = request.POST.get('color')
        price = request.POST.get('price')
        product_count = request.POST.get('product_count')
        category_id = request.POST.get('category_id')
        season_id = request.POST.get('season_id')
        product_composition_id = request.POST.get('product_composition_id')
        size_cloth_id = request.POST.get('size_cloth_id')
        size_shoes_id = request.POST.get('size_shoes_id')
        company_id = request.POST.get('company_id')


        category = Category.objects.get(id=category_id)             # Находим КАТЕГОРИЮ по соотв-щим идентификатору
        season = Season.objects.get(id=season_id)                   # Находим CЕЗОН по соотв-щим идентификатору
        product_composition = ProductComposition.objects.get(id=product_composition_id)  # СОСТАВ
        size_cloth = SizeCloth.objects.get(id=size_cloth_id)        # РАЗМЕР ОДЕЖДЫ
        size_shoes = SizeShoes.objects.get(id=size_shoes_id)        # РАЗМЕР ОБУВИ
        company = Company.objects.get(id=company_id)                # Производителя
                                                                    # т.е. получаем эти объекты по ID


        product = Product(                            # Создаем НОВЫЙ объект Product и передаем ему данные автомобиля
            name_prod=name_prod,
            article=article,
            description=description,
            color=color,
            price=price,
            product_count=product_count,
            category=category,
            season=season,
            product_composition=product_composition,
            size_cloth=size_cloth,
            size_shoes=size_shoes,
            company=company,
        )
        product.save()                                          # СОХРАНЯЕМ в БАЗЕ данных

        return HttpResponseRedirect(reverse('get-products'))
                                                # После сохранения перенаправляем на страницу со списком товаров.
                                                # reverse - возвращает "ИМЯ" URL, соответствующее указанному адресу.
                                                # т.е. reverse('get-products') = '/product/get-products/'

"""
Функция для поиска автомобилей по искомому параметру.

Параметры:
- request: объект HTTP-запроса

Возвращает:
- Если метод запроса 'GET', отображает шаблон 'companies/products.html'.
- Если метод запроса не 'GET',  то фильтрует объекты Car на основе "строки поиска" и отображает шаблон 
                                        'autopark/cars.html' с отфильтрованным списком автомобилей.
"""

def search_product(request):
    if request.method == 'GET':
        return render(request, 'companies/products.html')
    else:
        search_string = request.POST.get('search_string')
        product_list = Product.objects.filter(
            Q(name_prod__icontains=search_string)
            | Q(article__icontains=search_string)
            | Q(color__icontains=search_string)
            # | Q(price__icontains=search_string)
            | Q(category__name_category__icontains=search_string)
            | Q(season__name_season__icontains=search_string)
            | Q(product_composition__product_composition__icontains=search_string)
            | Q(size_cloth__size_cloth__icontains=search_string)
            | Q(size_shoes__size_shoes__icontains=search_string)
            | Q(company__name_company__icontains=search_string)
        )

        return render(request, 'companies/products.html', {'products': product_list})

# P.S: как ставить:
# Q(category__name_category__icontains=search_string)
# category - берем из: class Product(models.Model)
# name_category берем из: class Category(models.Model)

