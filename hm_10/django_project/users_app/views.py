from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm
from quotes_app.forms import AuthorEditForm, QuoteEditForm


def signup_user(request):
    if request.user.is_authenticated:
        return redirect(to="quotes_app:main")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes_app:main")
        else:
            return render(request, "users_app/signup.html", context={"form": form})

    return render(request, "users_app/signup.html", context={"form": RegisterForm()})


def login_user(request):
    if request.user.is_authenticated:
        return redirect(to="quotes_app:main")

    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is None:
            messages.error(request, "Username or password didn't match")
            return redirect(to="users_app:login")

        login(request, user)
        return redirect(to="quotes_app:main")

    return render(request, "users_app/login.html", context={"form": LoginForm()})


@login_required
def logout_user(request):
    logout(request)
    return redirect(to="quotes_app:main")


@login_required
def profile(request, username):
    user = request.user
    form_author = AuthorEditForm(request.POST)
    form_quote = QuoteEditForm(request.POST)

    if request.method == "POST":
        if form_author.is_valid():
            form_author.save()
        if form_quote.is_valid():
            form_quote.save()

    return render(
        request,
        "users_app/profile.html",
        {
            "form_quote": form_quote,
            "form_author": form_author,
            "user": user,
            "username": username,
        },
    )


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users_app/password_reset.html'
    email_template_name = 'users_app/password_reset_email.html'
    html_email_template_name = 'users_app/password_reset_email.html'
    success_url = reverse_lazy('users_app:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users_app/password_reset_subject.txt'
