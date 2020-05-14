from django.shortcuts import render
from django.contrib.auth.models import User
from social_django.models import *
from discovbeat.models import UserPlaylist, Song

import spotipy


def index(request):
	return render(request, 'discovbeat/index.html')

def getUserSocialId(user):
	return UserSocialAuth.objects.get(user=user)

def getToken(user):
	userSocialId=getUserSocialId(user)
	extraData=userSocialId.extra_data
	return extraData['access_token']


def dashboard(request):

	context_dict = {}
	context_dict["userPlaylist"]=[]

	userSocialId = getUserSocialId(request.user)
	username=userSocialId.uid
	extraData=userSocialId.extra_data

	token=extraData['access_token']

	userPlaylists={}
	sp = spotipy.Spotify(auth=token)
	offset=0
	while True:
		playlists = sp.user_playlists(user=username, limit=50, offset=offset)
		print(len(playlists["items"]))
		for playlist in playlists['items']:
			userPlaylists[playlist["name"]]=playlist
		if len(playlists["items"])<50:
			break
		else:
			offset+=50

	context_dict["userPlaylists"]=userPlaylists

	# print(i)
	# print(context_dict["userPlaylist"])
		#results = sp.playlist(playlist['id'], fields="tracks,next")
		# tracks = results['tracks']
		# print(tracks)
		# while tracks['next']:
		# 	tracks = sp.next(tracks)
		# 	print(tracks)

		# print(playlist['name'])

	return render(request, 'discovbeat/dashboard.html', context=context_dict)

def shareplaylist(request, playlist=None):
	context_dict={}
	songList=[]
	for key,value in request.POST.items():
		if key!="csrfmiddlewaretoken":
			playlist=eval(value)
			user = User.objects.get(username = request.user)
			newPlaylist=UserPlaylist(owner=user, name=playlist['name'],playlistId=playlist['id'],json=playlist)
			newPlaylist.save()
			token=getToken(request.user)
			sp = spotipy.Spotify(auth=token)
			results = sp.playlist(playlist['id'], fields="tracks,next")
			tracks = results['tracks']
			songList+=add_tracks(tracks,newPlaylist)
			while tracks['next']:
				tracks = sp.next(tracks)
				songList+=add_tracks(tracks,newPlaylist)

			for song in songList:
				print(song.name)
			context_dict['playlist']=newPlaylist
			context_dict['songList']=songList


	return render(request, 'discovbeat/shareplaylist.html', context=context_dict)

def add_tracks(results,playlist):
	songList=[]
	for item in results['items']:
		track = item['track']
		song = Song(playlist=playlist,name=track['name'],artist=track['artists'][0]['name'],album=track['album']['name'],songId=track['id'],json=track)
		song.save()
		songList.append(song)
	return songList
