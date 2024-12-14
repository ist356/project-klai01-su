from functions import get_account, get_summoner, get_league, get_match_id, get_matchdetail
import streamlit as st
import os
import pandas as pd

key = "RGAPI-37d0395b-8c96-4b4b-bb38-85fc4173f048"

st.set_page_config(layout="wide")

st.title("LoL Account Data")

locations = ["North America", "Korea", "Europe West"]

# region_mapping = {
#     "North America": {"routing": "AMERICAS", "platform": "NA1"},
#     "Korea": {"routing": "ASIA", "platform": "KR"},
#     "Europe": {"routing": "EUROPE", "platform": "EUW1"}
# }

location = st.selectbox("Select Region", locations)


# region_info = region_mapping[region]


game_name = st.text_input("Enter Game Name (e.g., Doublelift#NA1):")

if game_name:
    try:
        name, tagline = game_name.split("#", 1)
        if location == "North America":
            region = "AMERICAS"
            platform = "NA1"
        elif location == "Korea":
            region = "ASIA"
            platform = "KR"
        elif location == "Europe West":
            region = "EUROPE"
            platform = "EUW1"
        
        account = get_account(name, tagline, key, region)
        encrypted_puuid = account['puuid']

        summoner = get_summoner(encrypted_puuid, key, platform)
        encrypted_summonerid = summoner['id']

        league = get_league(encrypted_summonerid, key, platform)

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
        
        
        # match_id = get_match_id(encrypted_puuid, key)
        # match_detail = get_matchdetail(match_id[0], key)

        # gamelength_secs = match_detail['info']['gameDuration']

        # minutes = gamelength_secs // 60
        # remaining_seconds = gamelength_secs % 60

        # participants = match_detail['info']['participants']

        # selected_stats = [
        #     "summonerName", "championName", "champLevel", "kills", "deaths", "assists",
        #     "totalDamageDealtToChampions", "visionScore", "totalMinionsKilled",
        #     "item0", "item1", "item2", "item3", "item4", "item5", "item6"
        # ]

        # match_df = pd.DataFrame(participants)[selected_stats]

        # st.title("Match Details")
        # st.write(f"Game Duration: {minutes}m {remaining_seconds}s")
        # st.dataframe(match_df)
        

        # Assuming you already have a way to get match IDs and match details
        match_ids = get_match_id(encrypted_puuid, key, region)  # List of match IDs
        st.title("Match Details")
        
        # Function to display match details
        def display_match(match_id):
            match_detail = get_matchdetail(match_id, key, region)
            gamelength_secs = match_detail['info']['gameDuration']
            minutes = gamelength_secs // 60
            remaining_seconds = gamelength_secs % 60

            participants = match_detail['info']['participants']
            selected_stats = [
                "summonerName", "championName", "champLevel", "kills", "deaths", "assists",
                "totalDamageDealtToChampions", "visionScore", "totalMinionsKilled",
                "item0", "item1", "item2", "item3", "item4", "item5", "item6"
            ]

            match_df = pd.DataFrame(participants)[selected_stats]

            st.write(f"Game Duration: {minutes}m {remaining_seconds}s")
            st.dataframe(match_df)

        # Initialize the session state for match details visibility
        if 'match_details_visible' not in st.session_state:
            st.session_state.match_details_visible = {}

        # Display all match buttons and toggle visibility
        for idx, match_id in enumerate(match_ids):
            button_label = f"Match {idx + 1}"  # Label as Match 1, Match 2, etc.
            
            # Toggle visibility of match details when button is pressed
            if st.button(button_label, key=f"match_{idx}"):  # Assign unique keys to buttons
                if match_id in st.session_state.match_details_visible:
                    # If match details are already visible, hide them
                    st.session_state.match_details_visible[match_id] = not st.session_state.match_details_visible[match_id]
                else:
                    # If match details are not visible, show them
                    st.session_state.match_details_visible[match_id] = True

            # Show match details only if the corresponding button has been clicked
            if match_id in st.session_state.match_details_visible and st.session_state.match_details_visible[match_id]:
                # st.write(f"### Match {idx + 1} Details")  # Display header for match details
                display_match(match_id)  # Show the match details under the button

    except Exception as e:
        st.error(f"An error occurred: {e}")
