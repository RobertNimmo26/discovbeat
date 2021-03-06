from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('shareplaylist/', views.shareplaylist, name='shareplaylist'),
	path('submitshareplaylist/', views.submitshareplaylist,name='submitshareplaylist'),
	path('ajax/checkforuser', views.checkForUser, name='checkforuser'),
	path('ajax/saveComment',views.saveComment, name='savecomment'),
	path('ajax/saveLike',views.saveLike, name='savelike'),
	#path('ajax/generatePlaylist',views.generatePlaylist, name='generateplaylist'),
	path('ratePlaylist/', views.ratePlaylist, name='rateplaylist'),
	path('submitRatePlaylist/', views.submitRatePlaylist, name='submitrateplaylist'),
	path('playlistDashboard/', views.playlistDashboard, name='playlistdashboard'),
	path('playlistAnalysis/', views.playlistAnalysis, name='playlistanalysis'),
	path('instructions/', views.instructions, name='instructions'),
	path('contactus/', views.contactUs, name='contactus'),
	path('deletePlaylist/', views.deletePlaylist, name="deleteplaylist"),
	path('settings/', views.settings, name='settings'),
	path('deleteUser/', views.deleteUser, name="deleteuser"),
]