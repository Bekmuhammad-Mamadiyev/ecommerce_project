from django.urls import path

from apps.common.views import CountryView, RegionView

urlpatterns = [
    path('country/', CountryView.as_view()),
    path('region/', RegionView.as_view()),
]