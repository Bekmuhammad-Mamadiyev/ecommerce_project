from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.models import Country, Region
from apps.common.serializers import CountrySerializer, RegionSerializer

from rest_framework import viewsets

from .models import *
from .serializers import *


class MediaView(APIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class SettingsView(APIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class CountryView(APIView):
    def get(self, request):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)


class RegionView(APIView):
    def get(self, request):
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return Response(serializer.data)


class OurInstagramStoryView(APIView):
    queryset = OurInstagramStory.objects.all()
    serializer_class = OurInstagramStorySerializer


class CustomerFeedbackView(APIView):
    queryset = CustomerFeedback.objects.all()
    serializer_class = CustomerFeedbackSerializer
