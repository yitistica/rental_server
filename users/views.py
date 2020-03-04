from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .user_register import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from rental_services.urls import app_name as rental_service_app_name


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}.')
            return redirect(f'users:login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def home_page_with_redirect(request):
    if request.user.is_authenticated:
        return redirect(f'{rental_service_app_name}:service-main')
    else:
        return redirect(f'users:login')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'the account is updated.')
            return redirect(f'users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form,
               'p_form': p_form}

    return render(request, 'users/profile.html', context)

