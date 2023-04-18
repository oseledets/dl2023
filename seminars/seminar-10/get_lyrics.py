# GET IT HERE 
# https://docs.genius.com/#/undefined

# prerequisites 
# pip install git+https://github.com/johnwmillr/LyricsGenius.git

client_access_token = ""

import re
import lyricsgenius
from pathlib import Path

def clean_up(lyrics):
    junkwords = ["[Припев", "[Текст", "[Куплет", "[Предприпев", "[Интро", 
    "[Аутро", "[Рефрен", "[Интерлюдия", "[Постприпев", "[Бридж", "[Переход",
    "[Скит"]
    clean_lyrics = ''
    for line in lyrics.splitlines():
        if all(junk not in line for junk in junkwords):
            clean_lyrics += line + '\n'

    clean_lyrics = re.sub(r'\d+Embed','',clean_lyrics)
    
    return clean_lyrics

import lyricsgenius
LyricsGenius = lyricsgenius.Genius(client_access_token)

artist = LyricsGenius.search_artist("Manowar", max_songs=300)
lyrics = ''

for song in artist.songs:
    lyrics += clean_up(song.lyrics)
    lyrics += '\n\n[EOS]\n\n'

    with open("manowar_lyrics.txt", "w") as text_file:
        text_file.write(lyrics)