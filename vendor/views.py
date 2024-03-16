from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from .models import Vendor
from .forms import AddVendorForm
from accounts.forms import UserForm
from accounts.models import User, UserProfile

def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied

def register_vendor(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        vform = AddVendorForm(request.POST, request.FILES)
        if form.is_valid() and vform.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = vform.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()            
            messages.success(request, "Your account has been registered successfully! Please wait for the approval.")
            return redirect('register_vendor') 
        else:
            print(form.errors)
            
    vendor_form = AddVendorForm()
    user_form = UserForm()
    context = {
        'vform': vendor_form,
        'form': user_form,
    }
    return render(request, 'vendor/register-vendor.html', context)


@login_required(login_url='login')
@user_passes_test(test_func=check_role_vendor)
def vendor_dashboard(request):
    return render(request, 'vendor/dashboard.html')