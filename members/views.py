from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.views import View
from django.http import JsonResponse
from members.forms import RegisterUserForm, PasswordResetForm2, RegistrationAjaxForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Не правильное имя пользователя или пароль'))
            return redirect('login_user')
    else:
        return render(request, 'members/login_user.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'members/register_user.html', {
        'form': form,
    })


class PasswordResetView2(PasswordResetView):
    form_class = PasswordResetForm2


class LoginAjaxView(View):

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse(
                    data={
                        'status': 201
                    },
                    status=200
                )
            return JsonResponse(
                data={
                    'status': 400,
                    'error': 'Пароль и логин не валидные'
                },
                status=200
            )
        return JsonResponse(
            data={
                'status': 400,
                'error': 'Введите логин и пароль'
            },
            status=200
        )


class RegisterAjaxView(View):

    def post(self, request):
        form = RegistrationAjaxForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return JsonResponse(
                data={
                    'status': 201
                },
                status=200
            )
        return JsonResponse(
            data={
                'status': 400,
                'error': 'Проверьте введенные данные'
            },
            status=200
        )
