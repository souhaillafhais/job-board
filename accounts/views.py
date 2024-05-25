from django.shortcuts import render,redirect
from .forms import SignupForm , UserForm, ProfileForm,loginForm
from django.contrib.auth import authenticate,login as auth_login,logout
from .models import Profile
from django.urls import reverse





def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('accounts:profile')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = loginForm()
    return render(request, 'registration/login.html', {'form': form})


    

    
def logout_user(request):
    logout(request)
    return redirect('/')





def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        profileform = ProfileForm(request.POST)
        if form.is_valid() and profileform.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            auth_login(request, user)                         
            return redirect('/accounts/profile')    
    else: 
        form = SignupForm()
    return render (request,'registration/signup.html',{'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)

    
    return render(request,'accounts/profile.html',{'profile':profile})



def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid() :
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user =request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))   

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request,'accounts\profile_edit.html',{'userform':userform , 'profileform':profileform})



