from django.urls import path
from . import views

app_name = "posts" # url name below를 이용하기 위해 필요

urlpatterns = [
    path('', views.post_list, name = "list"), # url의 name을 list로 설정
    path('<int:pk>/', views.post_detail, name="detail"), # 지정한 type의 variable을 view 함수로 전달
    path('create/', views.post_create, name="create"),
    path('<int:pk>/update/', views.post_update, name="update"),
    path('<int:pk>/delete/', views.post_delete, name="delete")
]