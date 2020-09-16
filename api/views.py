from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import YoutubeVideo
from api.serializers import YoutubeSerializer

# Create your views here.
class GetYoutubeData(APIView):
    def get(self,requests,format=None):
        youtube = YoutubeVideo.objects.all().order_by('-video_publish_date')
        serilaizer_data = YoutubeSerializer(youtube,many=True)
        return Response(serilaizer_data.data,status=status.HTTP_200_OK)