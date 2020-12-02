from django.shortcuts import render
from deal_in.response import Response
from deal_in import transformer
from deal_in.jwt import JWTAuth
from django.db import models
from deal_in.models import TblUser
import json
from django.views.decorators.csrf import csrf_exempt
from deal_in.middleware import jwtRequired


@csrf_exempt
def index(request):
    if request.method == 'GET':
        user = TblUser.objects.all()
        user = transformer.transform(user)
        return Response.ok(values=user)
    elif request.method == 'POST':
        json_data = json.loads(request.body)
        user = TblUser()
        user.name = json_data['name']
        user.username = json_data['username']
        user.password = json_data['password']
        user.address = json_data['address']
        user.birth_date = json_data['birth_date']
        user.role = json_data['role']
        user.deleted = json_data['deleted']
        user.save()

        return Response.ok(
            values=transformer.userTransform(user),
            message="Added!"
        )


@csrf_exempt
def show(request, id):
    if request.method == 'GET':
        user = TblUser.objects.filter(id=id).first()

        if not user:
            return Response.badRequest(message='Pengguna tidak ditemukan!')

        user = transformer.userTransform(user)
        return Response.badRequest(values=user)
    elif request.method == 'PUT':
        json_data = json.loads(request.body)

        user = TblUser.objects.filter(id=id).first()
        if not user:
            return Response.badRequest(message="Pengguna tidak ditemukan")
        user.name = json_data['name']
        user.username = json_data['username']
        user.password = json_data['password']
        user.address = json_data['address']
        user.birth_date = json_data['birth_date']
        user.role = json_data['role']
        user.deleted = json_data['deleted']
        user.save()

        return Response.ok(
            values=transformer.userTransform(user),
            message="Updated!"
        )
    elif request.method == 'DELETE':
        user = TblUser.objects.filter(id=id).first()
        if not user:
            return Response.badRequest(message="Pengguna tidak ditemukan")

        user.delete()
        return Response.ok(message="Deleted!")
    else:
        return Response.badRequest(message="Invalid method!")


@csrf_exempt
def auth(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data['username']

        user = TblUser.objects.filter(username=username).first()

        if not user:
            return Response.badRequest(message='Pengguna tidak ditemukan!')

        if json_data['password'] != user.password:
            return Response.badRequest(message="Password atau email yang kamu masukkan salah!")

        user = transformer.userTransform(user)

        jwt = JWTAuth()
        user['token'] = jwt.encode({"username": user['username']})
        return Response.ok(values=user, message="Berhasil masuk!")
