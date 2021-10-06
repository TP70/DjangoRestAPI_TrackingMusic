from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrackListCreateView.as_view(), name="tracks"),
    path('seed-track/', views.TrackSeedView.as_view(), name="seed_track"),
    path('tracks/<int:pk>/', views.TrackDetailView.as_view(), name="track_detail"),
    path('recent-tracks/', views.RecentTracksListView.as_view(), name="recent_tracks"),
    path('artists/', views.ArtistListView.as_view(), name="artists"),
]
