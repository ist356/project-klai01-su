from test import get_account, get_summoner, get_league
import streamlit as st
import os

key = "RGAPI-c6d36bf4-db17-48f2-a385-0d35396d2c24"

st.title("Riot Games Account Information")
game_name = st.text_input("Enter Game Name (e.g., Doublelift#NA1):")

if game_name:
    try:
        name, tagline = game_name.split("#", 1)

        account = get_account(name, tagline, key)
        encrypted_puuid = account['puuid']

        summoner = get_summoner(encrypted_puuid, key)
        encrypted_summonerid = summoner['id']

        league = get_league(encrypted_summonerid, key)

        profile_icon_id = summoner['profileIconId']
        PROFILE_ICON_PATH = "data/dragon-14.24.1/14.21.1/img/profileicon/"
        profile_icon_path = os.path.join(PROFILE_ICON_PATH, f"{profile_icon_id}.png")


        st.header(f"**{account['gameName']}**#{account['tagLine']}")
        
        if os.path.exists(profile_icon_path):
            st.image(profile_icon_path, caption="Profile Icon", width=100)
        else:
            st.write("Profile icon not found.")
        
        st.write(f"**Level:** {summoner['summonerLevel']}")
        if league:
            st.write(
                f"**Rank:** {league[0]['tier']} {league[0]['rank']} - {league[0]['leaguePoints']} LP"
            )
        else:
            st.write("No information available.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
