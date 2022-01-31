from django.contrib import admin
from .models import Post

admin.site.register(Post) # Admin에서의 DB 관리 위해 model 등록