from rest_framework import serializers

from .models import Country, CustomerFeedback, Media, OurInstagramStory, Region, Settings


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ["id", "file", "type"]


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ["id", "home_image", "home_title", "home_subtitle"]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name", "code"]


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name", "region"]


class OurInstagramStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurInstagramStory
        fields = ["id", "image", "story_link"]


class CustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFeedback
        fields = [
            "id",
            "description",
            "rank",
            "customer_name",
            "customer_position",
            "customer_image",
        ]
