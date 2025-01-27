from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginUserForm


def register_page(request):
    if request.method == 'POST':

        form = CreateUserForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        print(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})


def login_page(request):
    form = LoginUserForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request=request, username=username, password=password)
        login(request, user)
        return redirect('/dashboard')
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)
