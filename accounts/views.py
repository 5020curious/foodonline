from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from .utils import detect_user


def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied
    

def register_user(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('my_account')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.role = User.CUSTOMER
            # user.set_password(password) 
            # form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "Your account has been registered successfully!")            
            return redirect('register_user')
        else:
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register-user.html', context)


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('my_account')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in.')
            return redirect('my_account')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')    
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('login')


@login_required(login_url='login')
def my_account(request):
    user = request.user
    redirect_url = detect_user(user)
    return redirect(redirect_url)


@login_required(login_url='login')
@user_passes_test(test_func=check_role_customer)
def accounts_dashboard(request):
    return render(request, 'accounts/dashboard.html')

