import requests
from api.models import YoutubeVideo
from youtube_api import YouTubeDataAPI
import datetime


def get_data():
    api_key = 'XXXXXXX'

    yt = YouTubeDataAPI(api_key)
    data_json = yt.search('django')

    for every_val in data_json:
        if YoutubeVideo.objects.filter(video_id=every_val['video_id']).exists():
            print("Video Already exists in db")
            continue
        else:
            datetime_time = datetime.datetime.fromtimestamp(every_val['video_publish_date'])
            video_entry = YoutubeVideo(video_id=every_val['video_id'],video_title=every_val['video_title'],video_description=every_val['video_description'],channel_title=every_val['channel_title'],video_thumbnail=every_val['video_thumbnail'],video_publish_date=datetime_time)
            video_entry.save()
            print("Video Added to db")

    return data_json
