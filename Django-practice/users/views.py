from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

def main(request):
    return render(request, "users/main.html")

class LoginView(View): # 함수로도 가능
    def get(self, request):
        form = LoginForm() # Empty form
        return render(request, "users/login.html", {"form":form}) # Shorthand

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid(): # 내부적으로 clean() 실행
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None: # 회원
                login(request, user)
                return render(request, "users/success.html")
            # return render(request, "users/login.html", {"form":form})
        return render(request, "users/login.html", {"form":form}) # invalid, 정보 담겨있는 Form

def log_out(request):
    logout(request)
    return redirect("users:main")