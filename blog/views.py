from django.shortcuts import render,redirect,reverse
from .models import Post
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import NewPostForm
from django.views import generic
from django.urls import reverse_lazy

# def post_list_view(request):
# posts_list = Post.objects.all()
#     posts_list = Post.objects.filter(statues='PUB').order_by('-datetime_modified')
#     return render(request,'blog/posts_list.html',{'posts_list': posts_list})
class PostlistView(generic.ListView):
    # model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'
    def get_queryset(self):
       return Post.objects.filter(statues='PUB').order_by('-datetime_modified')

# def post_detail_view(request, pk):
#     post=get_object_or_404(Post,pk=pk)
    #try:
    # post = Post.objects.get(pk=pk)
    #except Post.DoesNotExist:
    #   post=None
    #    print('exeept')

    # return render(request,'blog/post_detail.html',{'post':post})
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
# def postcreate_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:
#         form = NewPostForm()
#     return render(request, 'blog/post_create.html', context={'form': form})
       # post_title=request.POST.get('title')
       # post_text=request.POST.get('text')
       # user=User.objects.all()[0]
       # Post.objects.create(title=post_title,text=post_text,author=user , statues='PUB')
class PostCreateView(generic.CreateView):
      form_class = NewPostForm
      template_name = 'blog/post_create.html'



# def post_update_view(request,pk):
#
#     post=get_object_or_404(Post,pk=pk)
#     form = NewPostForm(request.POST or None,instance=post)
#     if form.is_valid():
#         print('hello')
#         form.save()
#         return redirect('posts_list')
#     return render(request,'blog/post_create.html', context={'form':form})
class PostUpdateView(generic.UpdateView):
      form_class = NewPostForm
      template_name = 'blog/post_create.html'
      model = Post

# def post_delete_view(request,pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#
#     return render(request,'blog/post_delete.html',context={'post':post})
class PostDeleteView(generic.DeleteView):
      model = Post
      template_name = 'blog/post_delete.html'
      success_url = reverse_lazy('posts_list')






