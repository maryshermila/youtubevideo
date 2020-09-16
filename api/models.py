from django.db import models

# Create your models here.
class YoutubeVideo(models.Model):
    video_id = models.CharField(max_length=100)
    video_title = models.TextField()
    video_description = models.TextField()
    channel_title = models.CharField(max_length=200)
    video_thumbnail = models.TextField()
    video_publish_date = models.DateTimeField()