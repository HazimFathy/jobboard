from django.urls import path , include
from . import views


app_name='blog'

urlpatterns = [
    path('',views.blog_list ),
    path('<int:id>', views.blog_detail,name='blog_detail'),
]