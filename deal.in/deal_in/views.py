from django.shortcuts import render, redirect


def login(request):
    return render(request, 'login/login.html')


def index(request):
    return render(request, 'content/index.html')


def deskripsi(request):
    return render(request, 'content/deskripsi.html')


def tentang(request):
    return render(request, 'content/about.html')
