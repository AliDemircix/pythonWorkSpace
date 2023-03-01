import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import os

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["SPOTIFY_CLIENT_ID"],
                                               client_secret=os.environ["SPOTIFY_SCRET_KEY"],
                                               scope="playlist-modify-private",
                                               redirect_uri="http://localhost:5001",
                                               show_dialog=True,
                                               cache_path=".cache"))

user_id = sp.current_user()["id"]
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

song_uris = []
year = date.split("-")[0]

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)

web_html = response.text

all_songs = BeautifulSoup(web_html, "html.parser")
get_song_titles = all_songs.select("li ul li h3")
# strip=True removes /t/p///
song_titles = [title.getText(strip=True) for title in get_song_titles]

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
