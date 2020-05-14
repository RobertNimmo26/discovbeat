from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserPlaylist(models.Model):
    sharedUser=models.ForeignKey(User,related_name="sharedUser",null=True,blank=True, on_delete=models.CASCADE)
    owner=models.ForeignKey(User,related_name="owner", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name= models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    playlistId= models.CharField(primary_key=True, blank=True,max_length=100)
    json=models.CharField(max_length=10000)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.playlistId)
        super(UserPlaylist, self).save(*args, **kwargs)

class Song(models.Model):
    playlist=models.ForeignKey(UserPlaylist, on_delete=models.CASCADE)
    rating=models.BooleanField(default=False)
    comment=models.CharField(max_length=300)
    name=models.CharField(max_length=100)
    album=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    songId= models.CharField(max_length=100, null=True)
    json=models.CharField(max_length=100000)
    songAutoId = models.BigAutoField(primary_key=True)
    slug = models.SlugField(unique=False)



    # In the future add restriction check

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.songAutoId)
        super(Song, self).save(*args, **kwargs)