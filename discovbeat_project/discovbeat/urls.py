from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('shareplaylist/', views.shareplaylist, name='shareplaylist'),
	path('submitshareplaylist/<int:playlistAutoId>/', views.submitshareplaylist,name='submitshareplaylist'),
]