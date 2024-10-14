from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView , DeleteView , UpdateView ,CreateView , DetailView
from .models import blog ,comment , category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import commentForm
# Create your views here.from django.shortcuts import render




class bloglist(ListView):
    model = blog
    template_name = "blog_list.html"
    ordering= ['-create_at']
    paginate_by = 4
    queryset = blog.objects.filter(active=True)
    



    
    
    
#add job def

def blog_detail ( request , id ) :
    blog_detail = blog.objects.get( id = id)
    comments=comment.objects.all()
    blog_list=blog.objects.all()
    category_list=category.objects.all()
    if request.method=='POST':
        form= commentForm(request.POST, request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.blog= blog_detail
            myform.owner= request.user
            myform.save()
            return redirect(reverse('blogs:blog'))
    else:
        form=commentForm()
        
    context = {'blog': blog_detail,'form':form , 'comments':comments,'blog_list':blog_list,'category_list':category_list}
    return render(request,'blog/blog_detail.html',context)
