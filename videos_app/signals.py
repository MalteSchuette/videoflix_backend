import django_rq
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Video


@receiver(post_save, sender=Video)
def trigger_video_processing(sender, instance, created, **kwargs):
    if created:
        queue = django_rq.get_queue('default')
        queue.enqueue('videos_app.tasks.process_video', instance.pk)
