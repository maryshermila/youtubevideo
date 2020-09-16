from rest_framework import serializers
from api.models import YoutubeVideo

class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = ('video_id','channel_title','video_title','video_description','video_thumbnail','video_publish_date')