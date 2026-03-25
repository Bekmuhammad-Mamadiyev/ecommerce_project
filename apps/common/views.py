from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.models import Country, Region
from apps.common.serializers import CountrySerializer, RegionSerializer


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