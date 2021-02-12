from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from django.contrib.auth.models import User


# Create your views here.

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('base.html')

    return render(request, 'signup.html', {'form': form})




#git config --global user.email "you@example.com"
#				git config --global user.name "Your Name"


'''
def signup(request):
    if request.method == 'Post':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('signup.html')
    else:
        return render(request,'signup.html')
  '''