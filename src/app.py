import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

# load the .env file variables
load_dotenv()

# making connection with the API
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id= client_id, client_secret= client_secret)

# making API requests

artisturl = '4gzpq5DPGxSnKTe4SA8HAU'
sp = spotipy.Spotify(auth_manager=auth_manager)
results = sp.artist_top_tracks(artisturl)

# extract name, popularity and duration in seconds

tracks = []
popularity = []
duration = []
for track in results['tracks'][:10]:
    tracks.append(track['name'])
    popularity.append(track['popularity'])
    duration.append(round(track['duration_ms']/1000/60, 2))

# transform request into DataFrame
songs = {"Track": tracks, "Popularity": popularity, "Duration": duration}
songs_df = pd.DataFrame(songs)

#Top 3 songs

songs_top_3 = songs_df[:3]
songs_top_3

# Analyzing statistical relationship with a plot

x = songs_df['Duration']
y = songs_df['Popularity']

plt.scatter(x, y)
plt.xlabel("DURATION")
plt.ylabel("POPULARITY")
plt.show()