from django.shortcuts import render
from django.contrib.auth.models import User
from social_django.models import *

import spotipy


def index(request):
	return render(request, 'discovbeat/index.html')

def dashboard(request):

	context_dict = {}
	context_dict["userPlaylist"]=[]

	userSocialId = UserSocialAuth.objects.get(user=request.user)
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
	for key,value in request.POST.items():
		if key!="csrfmiddlewaretoken":
			playlist=eval(value)
			print(playlist)
			print(key)
			print(playlist['id'])
	return render(request, 'discovbeat/shareplaylist.html')
