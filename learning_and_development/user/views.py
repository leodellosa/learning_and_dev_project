from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from .models import User
from django.db.models import Q
from django.contrib import messages
from learning_and_development.config import USER_API_URL,DJANGO_ENV, RUN_LOCAL
import requests
 
def index(request):
    return render(request, 'base.html')

def user_list(request):
    print(f"DJANGO_ENV: {DJANGO_ENV} and RUN_LOCAL: {RUN_LOCAL}")
    print(f"USER_API_URL: {USER_API_URL}")
    if DJANGO_ENV == 'production' and not RUN_LOCAL:
        base_url = f"{USER_API_URL}/users"
        try:
            response = requests.get(base_url)
            usersData = response.json()
            users = usersData.get('data', [])
            if response.status_code == 200:
                return render(request, 'user_list.html', {'users': users})
            else:
                messages.error(request, f"Error fetching users: {response.status_code}")
                return render(request, 'user_list.html', {'users': []})
        except requests.exceptions.RequestException as e:
            # print(e)
            messages.error(request, f"Error fetching users: {e}")
            return render(request, 'user_list.html', {'users': []})
    else:
        users = User.objects.all()
        query = request.GET.get('q', '')
        if query:
            user = User.objects.filter(Q(email__icontains=query))
        else:
            user = User.objects.all()

        return render(request, 'user_list.html', {'users': user,'query': query})

def user_detail(request, id):
    if (DJANGO_ENV == 'production') and not RUN_LOCAL:
        base_url = f"{USER_API_URL}/users/{id}"
        try:
            response = requests.get(base_url)
            user = response.json()
            if response.status_code == 200:
                # print(user)
                return render(request, 'user_detail.html', {'user': user})
            else:
                messages.error(request, f"Error fetching users: {response.status_code}")
                return render(request, 'user_list.html', {'user': []})
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Error fetching users: {e}")
    else:
        user = get_object_or_404(User, id=id)
        return render(request, 'user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'User added successfully!')
            return render(request, 'user_detail.html', {'user': user})
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"Error in {field.label}: {error}")
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def user_update(request, id):  
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'User updated successfully!')
            return render(request, 'user_detail.html', {'user': user})
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"Error in {field.label}: {error}")
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})
