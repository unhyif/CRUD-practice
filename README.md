# Overall process

After startproject, startapp

0. project > settings.py

- INSTALLED_APPS 에 app name 추가
- LANGUAGE_CODE = 'ko-KR', TIME_ZONE = 'Asia/Seoul'

1. project > urls.py

- from django.urls import path, include
  <br>urlpatterns에 path('app/', include('app.urls')) 등 추가
- app > urls.py 생성

2. app > models.py

```Python
class Table(models.Model):
    field_name = models.CharField(verbose_name="이름", max_length=100)

    def __str__(self):
          return self.field_name
```

cf) app > admin.py

```Python
from .models import Table
admin.site.register(Table)
```

3. app > urls.py

- from django.urls import path
  <br>from . import views
- app_name = "app"
- urlpatterns에 path('', views.index, name="index") 등 추가

4. app > views.py

```Python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Table
from .forms import FirstForm
```

(사전에 app > forms.py 생성 필요)

```Python
def index(request):
  objects = Table.objects.all()
  ctx = {"objects":objects}
  return render(request, template_name="app/index.html", context=ctx)
```

5. app > templates > app > index.html

```Html
{% for object in objects %}
 {{object.field_name}}
{% endfor %}
```

---

## CRUD

### Retrieve

- app > views.py
  <br>Table.objects.all() or Table.objects.filter(field_name="something") 등으로 objects 가져온 후 template에 전달

### Create

- app > forms.py 생성

```Python
from django import forms
from .models import Table
class FirstForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = "__all__"
```

- app.views.py
  <br>from .forms import FirstForm
  - if request.method == 'POST':
    <br>request.POST 이용하여 form object 생성,
    <br>validity check -> form.save() 후 redirect
  - else: empty form object 생성하여 template에 전달
- app > templates > app > create.html
  <br> POST 방식 `form`에 {{form}} 포함시킴

### Read

- app > urls.py : path('<int:pk>/')
- app > views.py
  <br>Table.object.get(id=pk) or get_object_or_404(Table, id=pk) 로
  <br> url에 입력된 pk와 일치하는 id를 가진 object 가져온 후 template에 전달

### Update

- app > urls.py : path('<int:pk>/update/')
- app > views.py
  - if request.method == 'POST':
    <br>request.POST와 instance keyword argument 이용하여 form object 생성,
    <br> validity check -> form.save() 후 pk 포함하여 redirect
  - else: instance k.a. 통해 기존 내용 반영된 form object 생성하여 template에 전달

### Delete

- app > urls.py : path('<int:pk>/delete/')
- app > views.py : 해당 object.delete() 후 redirect

---

## Authentication

- project > settings.py
  <br>AUTH_USER_MODEL = 'users.User'
- users > models.py

```Python
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
```

- users > forms.py
  <br>fields, clean method(check_password, raise forms.ValidationError)

- users > views.py

```Python
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

class LoginView(View): # login
  def get(self, request): # Empty form 전달
  def post(self, request):
    if form.is_valid(): #정보 담긴 form의 cleaned_data 이용하여 2차 authenticate
      if user is not None: login(request, user)
    else: # 정보 담긴 form 다시 전달

def log_out(request): #logout
    logout(request)
```

- users > urls.py

```Python
urlpatterns = [
    path('', views.main, name="main"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.log_out, name="logout")
]
```
