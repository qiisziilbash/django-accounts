from django.shortcuts import render


def sign_in(request):
    if request.method is 'GET':
        return render(request, 'accounts/Login.html')
    return None


def sign_up(request):
    if request.method is 'POST':
        return render(request, 'accounts/Register.html')
    return None
