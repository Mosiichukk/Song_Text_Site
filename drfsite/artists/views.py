from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404

import artists.views
from .models import *
from .serializers import ArtistSerializer

menu=["Головна","Пошук","Артисти"]
def index(request):
    return render(request, 'artists/index.html',{'title': 'Головна сторінка', 'menu':menu})

def about(request):
    return render(request,'artists/about.html',{'title': 'Про сайт', 'menu':menu})

def all_artists(request):
    artists=Artist.objects.all()
    return render(request,'artists/all_artists.html',{'title': 'Артисти', 'menu':menu, 'artists': artists})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    songs = Song.objects.filter(artist=artist)
    albums=Album.objects.filter(artist=artist)
    return render(request, 'artists/artist_detail.html', {'title': artist.name, 'menu':menu, 'artist': artist,'songs': songs,'albums':albums})

def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    lyric_text = get_object_or_404(Lyrics, pk=song_id)
    return render(request, 'artists/song_detail.html', {'song': song, 'title': song.title, 'menu':menu, 'lyric_text':lyric_text})

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    songs=Song.objects.filter(album_id=album_id)
    return render(request, 'artists/album_detail.html', {'album': album,'title': album.title, 'menu':menu,'songs':songs})

def search(request):
    query = request.GET.get('q', '').lower()
    artist_query, song_query = query, query


    if '-' in query:
        parts = query.split('-')
        if len(parts) == 2:
            artist_query, song_query = parts[0].strip(), parts[1].strip()

    # Фільтруйте артистів і пісні за відповідними запитами
    artists = Artist.objects.filter(name__icontains=artist_query)
    songs = Song.objects.filter(title__icontains=song_query)


    return render(request, 'artists/search_results.html', {'query': query, 'songs': songs, 'artists': artists, 'title':query})


# Create your views here.
class ArtistAPIView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

