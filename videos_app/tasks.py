from .models import Video


def process_video(video_id):
    video = Video.objects.get(pk=video_id)
    # FFMPEG processing will be implemented in Tag 8
    pass
