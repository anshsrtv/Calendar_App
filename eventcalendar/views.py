from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from calendarapp.forms import SignupForm
from calendarapp.models import Profile
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm

# def signup(request):
#     forms = SignupForm()
#     if request.method == 'POST':
#         forms = SignupForm(request.POST)
#         if forms.is_valid():
#             username = forms.cleaned_data['username']
#             password = forms.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('calendarapp:calendar')
#     context = {'form': forms}
#     return render(request, 'signup.html', context)

def signup(request):
   if request.method == 'POST':
       form = SignupForm(request.POST)
       if form.is_valid():
            user = form.save()
            # group = Group.objects.get(name='Guest') 
            # group.user_set.add(user)
            # user.save()
            Profile.objects.create(
                user=user,
                user_type='GST'
            )
            login(request, user)
            return redirect('calendarapp:calendar')
   else:
       form = SignupForm()
   return render(request,'signup.html',{'form':form})

def log_in(request):
   if request.method == 'POST':
       user=authenticate(request,username=request.POST['username'],
       password=request.POST['password'])
       if user is not None:
           login(request,user)
           return redirect('calendarapp:calendar')
       else:
           messages.error(request,'Invalid Credentials')
           return redirect('login')
   else:
       form = AuthenticationForm()
       return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('signup')