from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from .models import User
 
def index(request):
    return render(request, 'base.html')

def user_list(request):
    user = User.objects.all()
    return render(request, 'user_list.html', {'users': user})

def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user_detail.html', {'user': user})
