from rest_framework import serializers
from .models import *


class BannerSer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class AboutSer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class AgentSer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"


class Agent1Ser(serializers.ModelSerializer):
    class Meta:
        model = Agent1
        fields = "__all__"


class Agent2Ser(serializers.ModelSerializer):
    class Meta:
        model = Agent2
        fields = "__all__"


class PropertiesSer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = "__all__"


class TestimonialSer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class NewsSer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class ContactSer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ServicesSer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"
