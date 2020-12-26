from django.shortcuts import render, redirect
from functools import wraps
from deal_in.jwt import JWTAuth
from deal_in.response import Response
from django.http import HttpResponse


def jwtRequired(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            decode(args[0].headers.get('Authorization'))
        except Exception as e:
            return redirect('login_user')
        return fn(*args, **kwargs)

    return wrapper


def decode(token):
    token = str(token).split(' ')
    return JWTAuth().decode(token[1])
