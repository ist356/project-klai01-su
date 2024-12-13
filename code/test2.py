from test import get_account, get_summoner, get_league
from PIL import Image
import os

key = "RGAPI-c6d36bf4-db17-48f2-a385-0d35396d2c24"

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
profile_icon_id = summoner['profileIconId']

PROFILE_ICON_PATH = "/data/dragontail-14.24.1/14.21.1/img/profileicon/"
profile_icon_path = os.path.join(PROFILE_ICON_PATH, f"{profile_icon_id}.png")
image = Image.open(f'{profile_icon_path}')
image.show()

print(summoner['summonerLevel'])
print(league[0]['tier'] + " " + league[0]['rank'] + " " + str(league[0]['leaguePoints']) + " LP")