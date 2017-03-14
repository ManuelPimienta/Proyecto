from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    posts = Post.published.all()
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 post en cada página
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Si la pagina no es entero libera la primera 
        posts = paginator.page(1)
    except EmptyPage:
        # Si la pagina esta fuera de rango libera la ultima 
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html',
                    {'page': page,
                    'posts': posts})
    # posts = Post.published.all()
    # return render(request, 'blog/post/list.html',
    #                 {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)

    return render(request,
                    'blog/post/detail.html',
                    {'post': post})    