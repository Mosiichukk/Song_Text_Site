"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from artists import views
from artists.views import ArtistAPIView, index, about, all_artists, artist_detail, album_detail, song_detail, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/artistlist/', ArtistAPIView.as_view()),
    path('', index, name='index'),
    path('about/',about,name='about'),
    path('artists/',all_artists,name='all_artists'),
    path('artists/<int:artist_id>/', artist_detail, name='artist_detail'),
    path('song/<int:song_id>/', song_detail, name='song_detail'),
    path('album/<int:album_id>/', album_detail, name='album_detail'),
    path('search/', search, name='search'),

]
