from django.shortcuts import render , redirect
from .forms import signupform , profileform , UserForm
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.


#signup def
def signup(request):
    if request.method == 'POST':
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleanned_data.get('username')
            password= form.cleanned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('jobs:job_list'))
    else:
        form=signupform()
    return render(request,'registration/signup.html',{'form':form})

# profile def
def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})
    

#  profile edit def
def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
       profileform1 = profileform(request.POST,request.FILES,instance=profile)
       userform1 = UserForm(request.POST,instance=request.user)
       if  profileform1.is_valid() and userform1.is_valid():
           userform1.save()
           myprofile= profileform1.save(commit=False)
           myprofile.user=request.user
           myprofile.save()
           return redirect(reverse('accounts:profile'))
    else:
       profileform1 = profileform(instance=profile)
       userform1 = UserForm(instance=request.user)
    return render(request,'accounts/profile_edit.html',{'profileform1':profileform1, 'userform1':userform1})