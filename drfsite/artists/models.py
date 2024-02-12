from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.artist.name}"

class Song(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

class Lyrics(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE)
    lyric_text = models.TextField()

    def __str__(self):
        return f"Lyrics for {self.song.title}"

class Feature(models.Model):
    feature_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.feature_name} featuring {self.feature_artist.name} in {self.song.title}"


