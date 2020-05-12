from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class userPlaylist(models.Model):
    sharedUser=models.ForeignKey(User,related_name="sharedUser", on_delete=models.CASCADE)
    owner=models.ForeignKey(User,related_name="owner", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name= models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    playlistId= models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.playlistId)
        super(Quiz, self).save(*args, **kwargs)

class song(models.Model):
    playlist=models.ForeignKey(userPlaylist, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    rating=models.BooleanField(default=False)
    comment=models.CharField(max_length=300)
    name=models.CharField(max_length=100)
    album=models.CharField(max_length=100)
    artists=models.CharField(max_length=100)
    songId= models.CharField(primary_key=True, max_length=100)

    # In the future add restriction check

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.playlistId)
        super(Quiz, self).save(*args, **kwargs)