from django.shortcuts import render


def LoginView(request):
    return render(request, 'main/login.html')


def RegisterView(request):
    return render(request, 'main/register.html')



def RealgisterView(request):
    return render(request, 'main/register.html')