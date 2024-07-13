from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return render(request, "app_main/home.html")
    else:
        return redirect('login')


