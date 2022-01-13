from pyexpat import model
from django.db import models

class Post(models.Model): # Post라는 DB = class = table 생성 for data 객체화
    # table columns below
    title = models.CharField(verbose_name="제목", max_length=100) # verbose_name for human-readable column
    writer = models.CharField(verbose_name="글쓴이", max_length=50)
    content = models.TextField(verbose_name="내용")
    
    created_at = models.DateTimeField(auto_now_add=True) # When object is first created
    updated_at = models.DateTimeField(auto_now=True) # When object.save()
    # auto_now or auto_now_add to True => field to have editable=False and blank=True set
    
    def __str__(self): # instance가 문자열로 어떻게 표현될지, 필수 X
        return self.title