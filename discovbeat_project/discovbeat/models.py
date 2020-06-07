from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserPlaylist(models.Model):
    sharedUser=models.ForeignKey(User,related_name="sharedUser",null=True,blank=True, on_delete=models.CASCADE)
    owner=models.ForeignKey(User,related_name="owner", on_delete=models.CASCADE)
    slug = models.SlugField(unique=False)
    name= models.TextField()
    description = models.TextField()
    playlistId= models.TextField(blank=True, null=True)
    json=models.TextField()
    playlistAutoId = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.playlistAutoId)
        super(UserPlaylist, self).save(*args, **kwargs)

class Song(models.Model):
    playlist=models.ForeignKey(UserPlaylist, on_delete=models.CASCADE)
    description=models.TextField( null=True)
    rating=models.BooleanField(default=False)
    comment=models.TextField()
    name=models.TextField()
    album=models.TextField()
    artist=models.TextField()
    songId= models.TextField(null=True)
    json=models.TextField()
    songAutoId = models.BigAutoField(primary_key=True)
    slug = models.SlugField(unique=False)



    # In the future add restriction check

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.songAutoId)
        super(Song, self).save(*args, **kwargs)