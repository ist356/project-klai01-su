import requests
import pandas as pd

# constants
key = "RGAPI-6c6db368-1d25-4ea7-9244-a0f06bcbe898"

# game_name = input("Game name: ")

# name, tagline = game_name.split("#", 1)

# Add the '#' back to the tagline
# tagline = "#" + tagline

name="Doublelift"
tagline="NA1"
encrypted_puuid="T96L5S_fI5P8lD8yNpLGD3wN5kkrxWVDFcYHooE4wAUK7edEI2-MwydKdBR8Wb5XJ27KyREM36IHCw"


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

def get_match_id(encrypted_puuid, key):
    matchid_uri = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{encrypted_puuid}/ids?start=0&count=5&api_key={key}"
    response = requests.get(matchid_uri)
    response.raise_for_status()
    match_id = response.json()
    return match_id

def get_matchdetail(match_id, key):
    matchdetail_uri = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={key}"
    response = requests.get(matchdetail_uri)
    response.raise_for_status()
    match_data = response.json()
    return match_data

match_id = get_match_id(encrypted_puuid, key)

match_detail = get_matchdetail(match_id[0], key)

gamelength_secs = match_detail['info']['gameDuration']

minutes = gamelength_secs // 60
remaining_seconds = gamelength_secs % 60

print(f"{minutes}m {remaining_seconds}s")

participants = match_detail['info']['participants']

selected_stats = ["summonerName", "championName", "champLevel", "kills", "deaths", "assists", "totalDamageDealtToChampions", "visionScore", "totalMinionsKilled", "item0", "item1", "item2", "item3", "item4", "item5", "item6"]
match_df = pd.DataFrame(participants)[selected_stats]
# print(match_df)
