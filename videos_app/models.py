from django.db import models


class Video(models.Model):
    CATEGORY_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('documentary', 'Documentary'),
        ('horror', 'Horror'),
        ('sci-fi', 'Sci-Fi'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    video_file = models.FileField(upload_to='videos/raw/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
