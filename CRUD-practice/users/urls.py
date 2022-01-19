from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.main, name="main"),
    path('login/', views.LoginView.as_view(), name="login"),
    # as_view(): 진입 메소드
    # HTTP request의 종류 알아내어, 해당 이름을 갖는 메소드로 request 중계
    path('logout/', views.log_out, name="logout")
]