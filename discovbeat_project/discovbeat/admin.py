from django.contrib import admin
from discovbeat.models import UserPlaylist, Song

class UserPlaylistAdmin(admin.ModelAdmin):
    list_display = ('sharedUser','owner','slug','name','description','playlistId')

class SongAdmin(admin.ModelAdmin):
    list_display = ('playlist','rating','description','comment','name','album','artist','songId','songAutoId')


admin.site.register(UserPlaylist, UserPlaylistAdmin)
admin.site.register(Song, SongAdmin)
