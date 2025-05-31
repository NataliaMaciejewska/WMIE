from django.contrib.auth import login, authenticate, logout

from django.shortcuts import render, redirect


from .forms import LoginUserForm



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


def custom_logout(request):
    logout(request)
    return redirect('login')