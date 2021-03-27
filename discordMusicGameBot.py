import spotipy
import matplotlib
from spotipy.oauth2 import SpotifyClientCredentials

#access token dictionaries
discordAccessTokens = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI,
    'scope': 'identify email connections'
  } #not the correct tokens

spotifyAccessTokens = {
    'client_id': '88537321562449afb8875bf3d823e046',
    'client_secret': '4d306a0ee0114538953b7aa58c3c91f1',
  } 

geniusAccessTokens = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI,
    'scope': 'identify email connections'
  } #not the correct tokens

#other variables

url = "" #discord/spotify/genius
api = "" #discord/spotify/genius
playerScoreData = {
    'playerID' : score, #either their discord ID or just an abbreviated name. or perhaps their nickname
    'playerID' : score,
    'playerID' : score,
    'playerID' : score,
    #and so on
    }

#function prototypes

def apiHandshakes(api):
    #code here
    return #ture/false # if it successfully connects to either the specified api or we could try to connect to all at once

def getWebData(url):
    return #should import and return a (dictionary, .json, or other data structure) from the website api 

def randomizePlaylist():
    return #should return a randomized (dictionary, .json, or other data structure) of songs based on the imported one 

def connectToChannels(dictionary): 
    #tries to connect to one (or both channels depending on the gamemode) the bot's channel
    return #true/false succuess/fail

def readSpecifiedTextChannel():
    return #returns a string (or other data structure) of the name of the player who sent the message and the contents of that message

def command(string):
    #start a game, change a rule, whitelist a player(?), display a list of !commands in the designated 
    return #true/false if the command was enacted successfully

def startGame(int):
    return #starts the requested game type

def getPlayers():
    return #a dictionary(or another data structure) of all the participating players' discord names








#the code below is copied from https://github.com/plamere/spotipy
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(spotifyAccessTokens[client_id], spotifyAccessTokens[client_secret]))

#results = sp.search(q='weezer', limit=20)
#for idx, track in enumerate(results['tracks']['items']):
#    print(idx, track['name'])