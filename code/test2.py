from test import get_account, get_summoner, get_league
from PIL import Image
import os

# Doublelift#NA1
key = "RGAPI-37d0395b-8c96-4b4b-bb38-85fc4173f048"

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
# print(league)

