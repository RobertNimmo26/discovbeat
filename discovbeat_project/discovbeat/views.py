from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from social_django.models import *
from discovbeat.models import UserPlaylist, Song

import spotipy
import requests


def index(request):
	return render(request, 'discovbeat/index.html')

def instructions(request):
	return render(request, 'discovbeat/instructions.html')

def getUserSocialId(user):
	return UserSocialAuth.objects.get(user=user)

def getToken(user):
	userSocialId=getUserSocialId(user)
	extraData=userSocialId.extra_data
	return extraData['access_token']

@login_required
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
		for playlist in playlists['items']:
			userPlaylists[playlist["name"]]=playlist
		if len(playlists["items"])<50:
			break
		else:
			offset+=50

	context_dict["userPlaylists"]=userPlaylists

	deletePlaylists=UserPlaylist.objects.filter(owner=request.user, sharedUser=None)

	for i in deletePlaylists:
		i.delete()

	sharedPlaylists=UserPlaylist.objects.filter(owner=request.user)

	context_dict["sharedPlaylists"]=sharedPlaylists

	sharedToYouPlaylists=UserPlaylist.objects.filter(sharedUser=request.user)

	context_dict["sharedToYouPlaylists"]=sharedToYouPlaylists


	return render(request, 'discovbeat/dashboard.html', context=context_dict)

@login_required
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

def checkForUser(request):
	email = request.GET.get('email', None)
	data = {
		'exist': User.objects.filter(email__iexact=email, is_staff=False).exists()
	}
	print(data)
	return JsonResponse(data)

@login_required
def submitshareplaylist(request,playlistAutoId=None):
	print(playlistAutoId)
	if request.method == "POST":
		POST = request.POST.copy()

		playlist = UserPlaylist.objects.get(playlistAutoId=playlistAutoId)
		usershare=POST.pop("usershare")
		print(usershare)
		user=User.objects.get(email=usershare[0])
		description=POST.pop("description")
		playlist.sharedUser = user
		playlist.description = description[0]
		playlist.save()
		POST.pop("csrfmiddlewaretoken")

		for key, value in POST.items():
			songObject = Song.objects.get(songAutoId=key)
			songObject.description = value
			songObject.save()

	return redirect(dashboard)

@login_required
def ratePlaylist(request,playlistAutoId):
	context_dict={}
	playlist = get_object_or_404(UserPlaylist, playlistAutoId=playlistAutoId)
	songList = Song.objects.filter(playlist=playlist)
	context_dict['playlist']=playlist
	context_dict['songList']=songList

	return render(request, 'discovbeat/ratePlaylist.html', context=context_dict)

@login_required
def playlistDashboard(request):
	context_dict={}
	for key,value in request.POST.items():
		if key!="csrfmiddlewaretoken":
			playlist = UserPlaylist.objects.get(playlistAutoId=value)
			songLikedList = Song.objects.filter(playlist=playlist, rating=True)
			context_dict['playlist']=playlist
			context_dict['songLikedList']=songLikedList

	return render(request, 'discovbeat/playlistDashboard.html', context=context_dict)

# def generatePlaylist():
# 	playlistAutoId = request.GET.get('playlistAutoId', None)
# 	playlist = UserPlaylist.objects.get(playlistAutoId=playlistAutoId)
# 	song = Song.objects.filter(playlist=playlist, rating=True)
# 	songId
# 	endpoint_url = "https://api.spotify.com/v1/recommendations?"
# 	token = getUserSocialId(request.user)
# 	user_id = getToken(request.user)

# 	# OUR FILTERS
# 	market="UK"
# 	seed_genres="indie"
# 	target_danceability=0.9
# 	uris = [] 
# 	seed_artists = '0XNa1vTidXlvJ2gHSsRi4A'
# 	seed_tracks='55SfSsxneljXOk5S3NVZIW'

# 	# PERFORM THE QUERY
# 	query = f'{endpoint_url}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'
# 	query += f'&seed_artists={seed_artists}'
# 	query += f'&seed_tracks={seed_tracks}'

# 	response = requests.get(query, 
# 				headers={"Content-Type":"application/json", 
# 							"Authorization":f"Bearer {token}"})
# 	json_response = response.json()

# 	print('Recommended Songs:')
# 	for i,j in enumerate(json_response['tracks']):
# 				uris.append(j['uri'])
# 				print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

@login_required
def playlistAnalysis(request):
	context_dict={}
	for key,value in request.POST.items():
		if key!="csrfmiddlewaretoken":
			playlist = get_object_or_404(UserPlaylist, playlistAutoId=value)
			songList = Song.objects.filter(playlist=playlist)
			context_dict['playlist']=playlist
			context_dict['songList']=songList

	return render(request, 'discovbeat/playlistAnalysis.html', context=context_dict)

@login_required
def submitRatePlaylist(request):
	return redirect(dashboard)

def saveComment(request):
	songId = request.GET.get('songAutoId', None)
	comment = request.GET.get('comment', None)
	song = Song.objects.get(songAutoId=songId)
	song.comment=comment
	song.save()
	data = {
		'songAutoId': songId,
		'comment':comment
	}
	return JsonResponse(data)

def saveLike(request):
	songId = request.GET.get('songAutoId', None)
	like = request.GET.get('like', None)
	print(songId,like)
	song = Song.objects.get(songAutoId=songId)
	song.rating=like
	song.save()
	data = {
		'songAutoId': songId,
		'like':like
	}
	return JsonResponse(data)