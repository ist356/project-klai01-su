from test import get_account, get_summoner, get_league
from PIL import Image
import os

# Doublelift#NA1
key = "RGAPI-6c6db368-1d25-4ea7-9244-a0f06bcbe898"

game_name = input("Game name: ")
name, tagline = game_name.split("#", 1)

account = get_account(name, tagline, key)
encrypted_puuid = account['puuid']

summoner = get_summoner(encrypted_puuid, key)
encrypted_summonerid = summoner['id']

league = get_league(encrypted_summonerid, key)

print(account)
print("")
print(summoner)
print("")
print(league)

print(account['gameName']+account['tagLine'])

print(summoner['summonerLevel'])
print(league[0]['tier'] + " " + league[0]['rank'] + " " + str(league[0]['leaguePoints']) + " LP")

wins = league[0]['wins']
losses = league[0]['losses']
winrate = wins / (wins + losses) * 100
print(f"{wins}W {losses}L")
print(f"Winrate: {winrate:.0f}%")