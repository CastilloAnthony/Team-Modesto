import discord
from discord.ext import commands

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import os
import random
import json
import matplotlib

#arrays start at 0

#access token dictionaries
discordAccessTokens = {
    'client_id': '825473823751143424',
    'client_secret': '4aIFW7ESBbNLw2JLmnjk8oA_DC9OSJZn',
    'grant_type': 'authorization_code', #not quite sure what to put here V
    'code': code,
    'redirect_uri': REDIRECT_URI,
    'scope': 'identify email connections'
  } #not the correct tokens

spotifyAccessTokens = {
    'client_id': '88537321562449afb8875bf3d823e046',
    'client_secret': 'secret',
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
    } #and so on and on and on

playerMessageDataQueue = {
    'playerID' : message,
    }

listOfBotCommands = {                      #I don't think this is how commands work for discord -K
    'command1' : "!play gametype 1",
    'command2' : "!play gametype 2",
    'command3' : "!pause",
    'command4' : "!resume"
    }

discordTextChannel = "music" #or something else

client = commands.Bot(command_prefix = '!') #discord command start; I labeled it as client -K

@client.event               #Checks to see if bot it online/ready -K
async def on_ready(): 
    print("Bot is ready.")

#function prototypes below

def startGame(int): #kind of like our main()
    return #starts the requested game type

def apiHandshakes(api):
    #code here
    return #ture/false # if it successfully connects to either the specified api or we could try to connect to all at once

def connectToDiscordChannels(dictionary): 
    #tries to connect to one (or both channels depending on the gamemode) the bot's channel
    return #true/false succuess/fail

def getPlayers():
    return #a dictionary(or another data structure) of all the participating players' discord names

def getWebData(url):
    return #should import and return a (dictionary, .json, or other data structure) from the website api 

def randomizePlaylist():
    return #should return a randomized (dictionary, .json, or other data structure) of songs based on the imported one 

def readSpecifiedTextChannel(discordTextChannel):
    #input the playerID and the contents of that message into the playerMessageDataQueue dictionary
    return #maybe return the ammended dictionary (or other data structure)? 

def issueCommand(message):
    #change a rule
    #whitelist a player(?)
    #display a listOfBotCommands in the designated channel
    #!add playlist
    #!start gametype 1/2/3/4/???
    #!help
    #!players
    #!scoreboard
    #anything else
    return #true/false if the command was enacted successfully

def calculateScore(message):
    #we need to calculate their score
    #do they get partial credit?
    return #return the value of the score based on the inputted message


@commands.command()
async def create(self, ctx):
    """this is to create a json file"""
    user=str(ctx.author)
    id=str(ctx.author.id)
    with open('players.json') as f:
        users=json.load(f)
    if not id in users:
        await create(users, user, id)
        await ctx.send('player created')
        with open('players.json', 'w') as f:
            json.dump(users, f)

@commands.command()
async def get(self, ctx):
    with open('players.json') as f:
        users=json.load(f)
    await ctx.send(user[str(ctx.author.id)])
    
def create(players, user, id):
    players[id] = {}
    players[id]['name'] = user
    players[id]['score'] = 0 #inital score



#the code below is copied from https://github.com/plamere/spotipy
#from spotipy.oauth2 import SpotifyClientCredentials **I put it at the top -K
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(spotifyAccessTokens[client_id], spotifyAccessTokens[client_secret]))

query = "" #this should be all the songs from the playlist could be 
results = sp.search(query, limit=20)
for idx, track in enumerate(results['tracks']['items']):
    #print()#idx, track['name']
