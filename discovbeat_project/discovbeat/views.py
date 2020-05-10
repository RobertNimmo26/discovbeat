from django.shortcuts import render
from django.contrib.auth.models import User
from social_django.models import *

import spotipy


def index(request):
	return render(request, 'discovbeat/index.html')

def dashboard(request):
	print(request.user.id)
	print(UserSocialAuth._meta.fields)
	userSocialId = UserSocialAuth.objects.get(user=request.user)
	username=userSocialId.uid
	extraData=userSocialId.extra_data

	token=extraData['access_token']

	print(token)
	print(username)

	sp = spotipy.Spotify(auth=token)
	playlists = sp.user_playlists(username)
	for playlist in playlists['items']:
		results = sp.playlist(playlist['id'], fields="tracks,next")
		# tracks = results['tracks']
		# print(tracks)
		# while tracks['next']:
		# 	tracks = sp.next(tracks)
		# 	print(tracks)

		# print(playlist['name'])

	return render(request, 'discovbeat/dashboard.html')