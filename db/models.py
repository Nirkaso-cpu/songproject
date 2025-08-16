from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Singer/Band(models.Model):
    Singer/Band_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Song(models.Model):
    title = models.CharField(max_length=255)
    singer = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self) -> str:
        return self.title


class Stage(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row


class Concert(models.Model):
    show_time = models.DateTimeField()
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (
            f"{self.Song.title} "
            f"{self.show_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )
