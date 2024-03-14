from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages


def register_user(request):
    form = UserForm()
    if request.method == 'POST':
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
    context = {
        'form': form,
    }
    return render(request, 'accounts/register-user.html', context)


