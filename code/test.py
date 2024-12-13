import requests
import pandas as pd

# constants
key = "RGAPI-c6d36bf4-db17-48f2-a385-0d35396d2c24"

# game_name = input("Game name: ")

# name, tagline = game_name.split("#", 1)

# Add the '#' back to the tagline
# tagline = "#" + tagline

name="Doublelift"
tagline="NA1"



def get_account(name, tagline, key):
    accountv1 = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tagline}?api_key={key}"
    response = requests.get(accountv1)
    response.raise_for_status()
    accountv1_data = response.json()
    return accountv1_data


def get_summoner(encrypted_puuid, key):
    summonerv4 = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{encrypted_puuid}?api_key={key}"
    response = requests.get(summonerv4)
    response.raise_for_status()
    summonerv4_data = response.json()
    return summonerv4_data

def get_league(encrypted_summonerid, key):
    leaguev4 = f"https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{encrypted_summonerid}?api_key={key}"
    response = requests.get(leaguev4)
    response.raise_for_status()
    leaguev4_data = response.json()
    return leaguev4_data