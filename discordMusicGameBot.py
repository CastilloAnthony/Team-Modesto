import numpy

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
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI,
    'scope': 'identify email connections'
  } #not the correct tokens

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
    'playerID' : score,
    }

#function prototypes

def apiHandshakes(api):
    #code here
    return #ture/false # if it successfully connects to either the specified api or we could try to connect to all at once

def getWebData(url):
    return #should return a dictionary, .json, or other data structure from the website api 

def randomizePlaylist():
    return #should return a 

def readSpecifiedTextChannel():
    return #our bot will need to read the text chat for commands or player's guesses

def getPlayers():
    return #a dictionary(or another data structure) of all the participating players' discord names


