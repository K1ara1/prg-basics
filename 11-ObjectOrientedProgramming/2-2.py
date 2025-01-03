class Music:
    def __init__(self,artist,track_title,album,year):
       self.artist = artist
       self.track_title = track_title
       self.album = album
       self.year = year
    def __str__(self):
      return f"Performer: {self.artist} \nTitle: {self.track_title} \nAlbum: {self.album} \nYear: {self.year}"

music1 = Music('Gorillaz','November has come','Demon Days',2007)
music2 = Music('Fleetwood Mac','The Chain','Rumours',2004)
music1.__str__()
music2.__str__()

print(music1)
print(music2)