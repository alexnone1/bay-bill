from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .models import Account

def dashboard_view(request):
    all_account = Account.objects.all()

    context = {
        'accounts':all_account
    }
    return render(request, 'dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Authentication successful
            login(request, user)
            return redirect('dashboard')
        else:
            # Authentication failed
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
