from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from core.forms import RegisterForm, LoginForm, UserUpdateForm
from jobs.models import Job
from .models import User


def index(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("job_list")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {"form": form})


def login(request):
    message = ''
    form = LoginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('home')
        else:
            message = 'Username and password do not match. Please try again.'

    return render(request, 'login.html', {'form': form, 'message': message})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profiles/profile.html', {'user': user})


def update(request, username):
    if request.method == 'POST':
        print(request.FILES)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Profile Update Successfully!")
            return redirect('profile', request.user.username)
    else:
        user_form = UserUpdateForm(instance=request.user)

    return render(request, 'profiles/update.html', {
        "user_form": user_form,
    })


@login_required
def manage_posts(request, username):
    jobs = Job.objects.filter(posted_by__username=request.user.username).order_by('-created_at')
    paginator = Paginator(jobs, 4)
    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)
    return render(request, 'profiles/posts.html', {'page_obj': page_obj})

