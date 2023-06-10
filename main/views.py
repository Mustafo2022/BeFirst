from django.shortcuts import render


def HomeView(request):
    return render(request, 'main/main.html')


def AboutView(request):
    return render(request, 'main/about.html')

def RulesView(request):
    return render(request, 'main/rules.html')