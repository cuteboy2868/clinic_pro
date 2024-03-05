from django.shortcuts import render
from dashboard.models import User
from main.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import (logout
, authenticate, login)
from rest_framework.permissions import IsAuthenticated
from .tokens import *


@api_view(['POST'])
def signin_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                login(request, usr)
                tokens = get_tokens_for_user(usr)
                status = 200
                data = {
                    'status': status,
                    'username': username,
                    'token': tokens,
                }
            else:
                status = 403
                message = "Invalid Password or Username!"
                data = {
                    'status': status,
                    'message': message,
                }
        except User.DoesNotExist:
            status = 404
            message = 'This User is not defined!'
            data = {
                'status': status,
                'message': message
            }
        return Response(data)
    except Exception as err:
        return Response(f'{err}')

@api_view(['POST'])
def signup_view(request):
    username = request.POST.get('username')
    full_name = request.POST.get('full_name')
    password = request.POST.get('password')
    phone_number = request.POST.get('phone_number')
    new = User.objects.create_user(
        username=username,
        full_name=full_name,
        password=password,
        phone_number=phone_number,
    )
    ser = UserSer(new)
    return Response(ser.data)

@api_view(['PUT'])
def edit_view(request, pk):
    user = User.objects.get(pk=pk)
    username = request.POST['username']
    full_name = request.POST['full_name']
    password = request.POST['password']
    phone_number = request.POST['phone_number']
    address = request.POST['address']
    user.username = username
    if full_name is not None:
        user.full_name = full_name
    if phone_number is not None:
        user.phone_number = phone_number
    if address is not None:
        user.address = address
    if password is not None:
        user.set_password(password)
    ser = UserSer(user)
    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    login(request)
    return Response({'data':'success'})

