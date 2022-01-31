from django.shortcuts import render, redirect, get_object_or_404
from .models import Post # DB에 접근 가능해짐 ✔
from .forms import PostForm # Post object 만들 수 있는 form object

def post_list(request): # request object
    posts = Post.objects.all() # DB의 Post objects 가져옴
    ctx = {'posts':posts}
    return render(request, template_name="posts/list.html", context=ctx) # object 자체 말고 딕셔너리 형태로 전달
# Render = send http response

def post_detail(request, pk):
    post = Post.objects.get(id=pk) # id = Django가 automatically 생성한 object의 primary key
    # post = get_object_or_404(Post, id=pk) 도 가능
    ctx = {'post':post}
    return render(request, template_name="posts/detail.html", context=ctx)


# def post_create(request):
#     if request.method == 'POST':
#         post = Post() # Post object 생성 (DB 변경 X)
#         post.title = request.POST['title'] # 사용자가 submit한 정보로 object 완성
#         post.writer = request.POST['writer']
#         post.content = request.POST['content']
#         post.save() # DB에 등록 -> migrate 필요
#         return redirect("posts:list")
#     else: # Show empty form
#         return render(request, template_name="posts/create.html")

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = PostForm() # Empty form object
        ctx = {"form":form}
        return render(request, template_name="posts/create-form.html", context=ctx)

def post_update(request, pk):
    post = get_object_or_404(Post, id=pk) # id가 pk인 Post object
    if request.method == 'POST': # DB 변경
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save() # Update the existing instance
        return redirect("posts:detail", pk)
    else: # 수정
        form = PostForm(instance = post) # Accept an existing instance
        ctx = {'form':form}
        return render(request, template_name="posts/create-form.html", context=ctx)

def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect("posts:list")