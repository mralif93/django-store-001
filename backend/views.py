from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .forms import CustomerForm, PurchaseForm
from .models import Customer, Purchase
import bcrypt

# Create your views here.
def DashboardView(request):
    context = {}
    return render(request, 'backend/dashboard.html', context)

def UsersView(request):
    users = Customer.objects.all()
    context = {
        'users': users
    }
    return render(request, 'backend/users.html', context)

def UserAddView(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        saved = form.save(commit=False)
        saved.is_active = True
        saved.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(10)).decode()
        saved.save()

        messages.success(request, 'Successfully create new user.')
        return redirect('users_view')
    context = {
        'form': form,
    }
    return render(request, 'backend/user_add.html', context)


def UserUpdateView(request, id):
    user = Customer.objects.get(id=id)
    if user is None:
        messages.warning(request, "Sorry, didn't find any user. Please try again.")
        return redirect('users_view')
    
    form = CustomerForm(request.POST or None, instance=user)
    if form.is_valid():
        saved = form.save(commit=False)
        if request.POST['password'] is not None:
            saved.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(10)).decode()
        saved.updated = datetime.now()
        saved.save()
        
        messages.success(request, 'Successfully update user details.')
        return redirect('users_view')

    context = {
        'form': form
    }
    return render(request, 'backend/user_update.html', context)