from django.shortcuts import render
# Импортируем http
from django.http import HttpResponse
import random
import string

# 3. Создаем функцию
# request - то, что пользователь ищет(?)
def home(request):
    # 4. Подключаем шаблоны к функции представления
    # render позволяет возвращать шаблоны в виде HttpResponse
    return render(request, 'generator/home.html')

def password(request):

    characters = string.ascii_lowercase

    # Будет брать переменную из запроса в адресной строке
    lenght = int(request.GET.get('lenght', 12))

    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase

    if request.GET.get('special'):
        characters += string.punctuation

    if request.GET.get('numbers'):
        characters += string.digits

    the_password = ''
    for i in range(lenght):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':the_password})

def about(request):
    return render(request, 'generator/about.html')