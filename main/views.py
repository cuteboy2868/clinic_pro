from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from models import *
from serializers import *

# Create your views here.
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialazer import *


@api_view(['GET'])
def get_banner(request):
    banner = Banner.objects.last()
    ser = BannerSer(banner)
    return Response(ser.data)


@api_view(['GET'])
def get_proper(request):
    proper = Properties.objects.all().order_by('-id')[:6]
    ser = PropertiesSer(proper, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_about(request):
    about = About.objects.all().order_by('-id')[:3]
    ser = AboutSer(about, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_agent1(request):
    agent1 = Agent1.objects.last()
    ser = Agent1Ser(agent1)
    return Response(ser.data)


@api_view(['GET'])
def get_agent(request):
    agent = Agent.objects.all().order_by('-id')[:3]
    ser = AgentSer(agent, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_agent2(request):
    agent2 = Agent2.objects.last()
    ser = Agent2Ser(agent2)
    return Response(ser.data)


@api_view(['GET'])
def get_services(request):
    services = Services.objects.all().order_by('-id')[:6]
    ser = ServicesSer(services, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_testimonial(request):
    testimonial = Testimonial.objects.all().order_by('-id')[:4]
    ser = TestimonialSer(testimonial, many=True)
    return Response(ser.data)




@api_view(['POST'])
def get_contact(request):
   full_name = request.POST['full_name']
   last_name = request.POST['last_name']
   email = request.POST['email']
   contact = Contact.objects.create(
       full_name=full_name,
       last_name=last_name,
       email=email,
   )
   ser = ContactSer(contact)
   return Response(ser.data)










@api_view(['GET'])
def get_news(request):
    news = News.objects.all().order_by('-id')[:3]
    ser = NewsSer(news, many=True)
    return Response(ser.data)