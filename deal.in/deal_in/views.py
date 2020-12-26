from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from deal_in.middleware import jwtRequired
from deal_in.jwt import JWTAuth
import json
import requests
from pprint import pprint


def login(request):
    if 'jwt' in request.COOKIES:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            data = {"username": username, "password": password}
            response = requests.post(
                'http://127.0.0.1:8000/api/user/login/', json=data)
            result = []
            result.append(response.json())
            if result[0]['values'] != []:
                # request.session['token'] = result[0]['values']['token']
                res = redirect("home")
                res.set_cookie(
                    'jwt', result[0]['values']['token'], max_age=60)
                return res
            else:
                messages.error(request, result[0]['message'])
                return redirect("login_user")
        context = {
            'title': 'Login | DeaL.In'
        }
        return render(request, 'login/login.html', context)


def logout(request):
    res = redirect('login_user')
    res.delete_cookie('jwt')
    return res


def signup(request):
    if 'jwt' in request.COOKIES:
        return redirect("home")
    else:
        if request.method == 'POST':
            name = request.POST['name']
            username = request.POST['username']
            address = request.POST['address']
            birth_date = request.POST['birth_date']
            role = request.POST['role']
            password = request.POST['password']
            data = {
                "name": name,
                "username": username,
                "address": address,
                "birth_date": birth_date,
                "id_role": role,
                "password": password
            }
            response = requests.post(
                'http://127.0.0.1:8000/api/user/signup', json=data)
            result = []
            result.append(response.json())
            if result[0]['values'] != None:
                messages.error(request, result[0]['message'])
                return redirect('login_user')
            else:
                messages.error(request, "Isi Data Sesuai Aturan")
                return redirect('signup_user')
        context = {
            'title': 'Signup | DeaL.In'
        }
        return render(request, 'login/signup.html', context)


def index(request):
    if 'jwt' in request.COOKIES:
        jwt = JWTAuth()
        username = jwt.decode(request.COOKIES['jwt'])
        context = {
            'user': username['username']
        }
        return render(request, 'content/index.html', context)
    else:
        return render(request, 'content/index.html')


def deskripsi(request):
    return render(request, 'content/deskripsi.html')


def tentang(request):
    return render(request, 'content/about.html')


def detail_user(request, id):
    context = {
        'response': requests.get(
            'http://127.0.0.1:8000/api/user/show/'+id).json()
    }
    return render(request, 'content/detail_user.html', context)
