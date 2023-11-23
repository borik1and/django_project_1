# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def about(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(f'имя: {name}, имеил: {email}, сообщение: {message}.')
        with open('message.txt','a') as t_f:
            t_f.write(f'имя: {name}, имеил: {email}, сообщение: {message}.')
    return render(request, 'catalog/about.html')
