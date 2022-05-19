from django.shortcuts import render
from django.http import HttpResponse


# тут только "логика" - функции для обработки и возврат данных


def index(request):
    # return HttpResponse("Это чистая индекс страница")
    context = {

    }
    return render(request, 'app_student/pages/index.html', context)


def home(request):
    context = {

    }
    return render(request, 'app_student/pages/home.html', context)


def login(request):
    context = {

    }
    return render(request, 'app_student/pages/login.html', context)


def about(request):
    context = {

    }
    return render(request, 'app_student/pages/about.html', context)


def list(request):
    context = {

    }
    return render(request, 'app_student/pages/list.html', context)


def origin_home(request):
    context = {

    }
    return render(request, 'app_student/pages/origin_home.html', context)


def CreatePage(request):
    context = {

    }
    return render(request, 'app_student/pages/CreatePage.html', context)

def todo_create(request):
    if request.method == "POST":
        print("это POST запрос")

        # приём и обработка данных
    context = {}
    return render(request, 'app_student/pages/CreateTodo.html', context)


def todo_detail(request):

    print(request)
    if request.method == "GET":
        print("Это GET запрос")
    if request.method == "POST":
        print("Это GET запрос")
    if request.method == "PUT":
        print("Это GET запрос")
    if request.method == "DELETE":
        print("Это GET запрос")

    # print("request.method: ", request.method)
    # print("request.path: ", request.path)
    # print("request.headers: ", request.headers)
    # print("request.META: ", request.META)
    # print("request.data: ", request.data)
    # print("request.GET: ", request.GET)


    is_completed = False
    if is_completed:
        pass
    else:
        pass

    list = [1, 2, 3]
    for i in list:
        index = list.index(i)
        print(i)

    context = {"title": "1. Закуп продуктов на неделю", "description": "Овощи, Фрукты, Ягоды, Орехи, Зелень, Рыба, Замороженные заготовки"
        }
    return render(request, 'app_student/pages/DetailTodo.html', context)
