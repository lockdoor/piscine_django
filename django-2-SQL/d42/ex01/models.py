from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True)  # Unique, 64-byte max, non-null
    episode_nb = models.BigAutoField(primary_key=True)  # Full, primary key
    opening_crawl = models.TextField(null=True, blank=True)  # Text, can be null, no size limit
    director = models.CharField(max_length=32)  # 32-byte max, non-null
    producer = models.CharField(max_length=128)  # 128-byte max, non-null
    release_date = models.DateField()  # Date, non-null
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

