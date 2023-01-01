from django.shortcuts import *
from .models import *


# Create your views here.
def show_blog(request):
    blogs = Blog.objects
    return render(request, 'blogs/blog.html', {'blogs': blogs})


def post_detail(request, post_id):
    post_info = get_object_or_404(Blog, pk=post_id)
    return render(request, 'blogs/blog_info.html', {"post_info": post_info})

