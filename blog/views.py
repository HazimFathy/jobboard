from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from .models import blog
from django.core.paginator import Paginator

# Create your views here.
def blog_list(request):
    blog_list= blog.objects.all()
    
    paginator = Paginator(blog_list, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context ={'blogs':page_obj}
    return render(request,'blog/blog_list.html',context)


def blog_detail(request, id):
    blog_detail = blog.objects.get(id=id)
    context={'blog':blog_detail}
    return render(request,'blog/blog_detail.html',context)
