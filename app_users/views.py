from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.http import HttpResponse


User = get_user_model()
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')  # This should be 'password', not 'username'

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'app_users/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'app_users/login.html')


def logout_user(request):
    logout(request)
    return redirect("login")

def register_user(request):
    if request.POST:
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if username and password1 and password2 and password1 == password2:
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email
            )

            user.set_password(password2)
            user.save()
            return redirect("login")
    return render(request, 'app_users/register.html')

