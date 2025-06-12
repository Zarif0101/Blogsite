from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm, UserProfileChange  # your custom form

# Create your views here.

def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    context = {'form': form, 'registered': registered}
    return render(request, 'App_Login/signup.html', context=context)


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Index'))
    return render(request, 'App_Login/login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Index'))


@login_required
def profile(request):
    return render(request, 'App_Login/profile.html', context={})



@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/change_profile.html', context={'form': form})


@login_required
def pass_change(request):
    current_user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/pass_change.html', context={})