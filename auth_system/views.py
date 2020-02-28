from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegisterForm

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Testing to authenticate user after signup
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, '''You account has been created. 
                                    You can fill your profile details''')
            return redirect('edit-user-profile')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'auth_system/signup.html', context)