from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# from .forms import UserRegistrationForm

# from django.core.exceptions import ValidationError
# from django.contrib import messages



# <!-- 1 Вариант через MODAL window for REGISTRATION -->

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists(): # проверка на существование пользователя по имени #
            return HttpResponseRedirect(reverse('get-products')) # ИНАЧЕ перенаправляем на страницу с продуктами!

        if User.objects.filter(email=email).exists(): # проверка на существование пользователя по email #
            return HttpResponseRedirect(reverse('get-products'))

        if not username or not email or not password or not confirm_password: # Проверка, чтобы не было пустых полей!
            return HttpResponseRedirect(reverse('get-products'))  # Иначе перенаправляем на страницу с продуктами

        if password != confirm_password:
            return HttpResponseRedirect(reverse('get-products'))

        group_user = Group.objects.get(name='users')

        user = User.objects.create_user(username, email, password)
        user.groups.add(group_user)
        user.save()
        # login(request, user) # (Вместо - user.save()) Так можно сделать, если хотим сразу после регистрации "ВОЙТИ НА САЙТ!"

        return HttpResponseRedirect(reverse('get-products'))
        # return HttpResponseRedirect(reverse('login_user'))
    else:
        return HttpResponseRedirect(reverse('get-products'))


# <!-- 2 Вариант через MODAL window for REGISTRATION  через FORMs.py -->

# def signup(request):
#
#     if request.method == 'POST':
#         form = UserRegistrationForm()
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return HttpResponseRedirect(reverse('get-products'))
#         else:
#             return HttpResponseRedirect(reverse('get-products'))
#
#     else:
#         return HttpResponseRedirect(reverse('get-products'))




# <!-- РЕГИСТРАЦИЯ через ШАБЛОН signup.html -->

# def signup(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#
#         group_user = Group.objects.get(name='users')
#
#         user = User.objects.create_user(username, email, password)
#         user.groups.add(group_user)
#         user.save()
#
#         return HttpResponseRedirect(reverse('login_user'))
#     else:
#         return render(request, 'userAdmin/signup.html')



# ПРОБНЫЙ ВАРИАНТ

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']
#
#         try:
#             if not username or not password or not email:
#                 raise ValidationError('Все поля должны быть заполнены!')
#
#             if User.objects.filter(username=username).exists():
#                 raise ValidationError('Пользователь с таким именем уже существует!')
#
#             if User.objects.filter(email=email).exists():
#                 raise ValidationError('Такой Email уже зарегистрирован!')
#
#             if len(password) < 4:
#                 raise ValidationError('Минимальная длина пароля 4 символа!')
#
#             if password != request.POST['confirm_password']:
#                 raise ValidationError('Пароли не совпадают!')
#
#             group_user = Group.objects.get(name='users')
#
#             user = User.objects.create_user(username=username, password=password, email=email)
#
#             user.groups.add(group_user)
#             user.save()
#
#             messages.success(request, 'Регистрация прошла успешно!')
#
#             # return HttpResponseRedirect(reverse('login'))
#             return HttpResponseRedirect(reverse('get-products'))
#
#         except ValidationError as e:
#             error = str(e)
#             # return render(request, 'userAdmin/register.html', {'error': error})
#             return HttpResponse('#regModal', {'error': error})
#     else:
#         return HttpResponseRedirect(reverse('get-products'))



# <!-- через MODAL window for LOGIN -->

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('get-products'))

        # < !-- если пользователь с таким именем/паролем НЕ существует -->
        return HttpResponseRedirect(reverse('get-products'))

    else:
        return HttpResponseRedirect(reverse('get-products'))


# <!-- через ШАБЛОН login.html -->
# def login_user(request: HttpRequest):
#     if request.method == 'POST':
#         username = request.POST['userName']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse('get-products'))
#
#         return render(request, 'userAdmin/login.html')
#
#     else:
#         return render(request, 'userAdmin/login.html')


def logout_user(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse('get-products'))
