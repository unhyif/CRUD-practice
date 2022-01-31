from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # Post의 schema가 담긴 form = Post object를 생성/수정할 수 있음
        fields = "__all__"