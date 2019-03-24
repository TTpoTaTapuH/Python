from django.shortcuts import render
from .forms import StartPage, Authorization
from django.http import HttpResponse
from .models import Users
# Create your views here.

def index(request):
    start_page = StartPage()
    if request.method == "POST":
        start_page = StartPage(request.POST)
        if start_page.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            try:
                user = Users.objects.get(email=email)
                if user.email==email and user.password==password:
                    return HttpResponse("<h2>Добро пожаловать на наш сайт!</h2><p>{0} {1}</p>".format(email, password))
                else:
                    return HttpResponse("<h2>Логин или почта неправильна!</p>")
            except Users.DoesNotExist:
                return HttpResponse("<h2>Такого пользователя нет!</p>")
    return render(request, "welcome/index.html", {"form": start_page})

def registration(request):
    reg_page = Authorization()
    if request.method == "POST":
        reg_page = Authorization(request.POST)
        if reg_page.is_valid():
            user = Users()
            user.email = request.POST.get("email")
            user.password = request.POST.get("password")
            user.name = request.POST.get("name")
            user.surname = request.POST.get("surname")
            user.telephone = request.POST.get("telephone")
            user.gender = request.POST.get("gender")
            user.date_birthday = request.POST.get("date_birthday")
            user.save()
            comp = Users.objects.all()
            return render(request, "welcome/registration.html", {"user": comp})
    return render(request, "welcome/registration.html", {"form": reg_page})