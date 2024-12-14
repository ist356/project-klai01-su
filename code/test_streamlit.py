from test import get_account, get_summoner, get_league
import streamlit as st
import os

key = "RGAPI-6c6db368-1d25-4ea7-9244-a0f06bcbe898"

st.title("LoL Account Data")
game_name = st.text_input("Enter Game Name (e.g., Doublelift#NA1):")

if game_name:
    try:
        name, tagline = game_name.split("#", 1)

        account = get_account(name, tagline, key)
        encrypted_puuid = account['puuid']

        summoner = get_summoner(encrypted_puuid, key)
        encrypted_summonerid = summoner['id']

        league = get_league(encrypted_summonerid, key)

        profile_icon_id = str(summoner['profileIconId'])
        PROFILE_ICON_PATH = '../project-klai01-su/data/dragontail-14.24.1/14.24.1/img/profileicon/'
        profile_icon_path = PROFILE_ICON_PATH + profile_icon_id + '.png'
        

        st.subheader(f"**{account['gameName']}**#{account['tagLine']}")
        
        if os.path.exists(profile_icon_path):
            st.image(profile_icon_path, width=128)
        else:
            st.write("Profile icon not found.")
        
        st.write(f"**Level:** {summoner['summonerLevel']}")

        st.write(f"**Ranked Stats:**")
        if league:
            for i in range(len(league)):
                wins = league[i]['wins']
                losses = league[i]['losses']
                winrate = wins / (wins + losses) * 100
                
                st.write(f"""
                        **{league[i]['queueType']}:**  
                        {league[i]['tier']} {league[i]['rank']} - {league[i]['leaguePoints']} LP  
                        {wins}W {losses}L  
                        Win rate: {winrate:.0f}%  
                        """)
                
        else:
            st.write("No data available.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
