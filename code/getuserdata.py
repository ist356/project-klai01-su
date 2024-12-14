import cassiopeia as cass
import pandas as pd
# import streamlit as st

cass.set_riot_api_key("RGAPI-37d0395b-8c96-4b4b-bb38-85fc4173f048")

account = cass.get_account(name="Doublelift", tagline="NA1", region="NA")
summoner = account.summoner

print(account.name_with_tagline)
print()
# print(summoner.level)
# print(summoner.profile_icon.id)
# print(summoner.ranks)

print(summoner.match_history)
'''
print("{name}\nLevel: {level}".format(name=account.name_with_tagline, 
                                      level=summoner.level,
                                      
                                      ))
'''

# a_summoner = Summoner(puuid=acc_puuid, region="NA")
# print(a_summoner)
# print(a_summoner.champion_masteries, a_summoner.match_history, a_summoner.current_match, a_summoner.leagues)



'''
print("{name} level {level} summoner on the {region} server.".format(name=account.name_with_tagline,
                                                                          level=summoner.level,
                                                                          region=summoner.region))                                     
'''
'''
st.title("League of Legends Player Info")

# Input: Riot ID (Name + Tagline)
riot_name = st.text_input("Enter Riot ID Name (e.g., Doublelift):")
riot_tagline = st.text_input("Enter Tagline (e.g., NA1):")
riot_region = st.text_input("Enter Region (e.g., NA):")

if riot_name and riot_region and riot_region:
    try:
        # Fetch Summoner information using Riot ID
        summoner = cass.get_account(name=riot_name, tagline=riot_tagline, region=riot_region.upper())
        
        # Display Summoner details
        st.subheader("Summoner Info")
        st.write(f"**Name:** {account.name_with_tagline}")
        st.write(f"**Level:** {account.level}")
        st.write(f"**Profile Icon ID:** {summoner.profile_icon.id}")
        
        # Fetch Ranked details
        rank_info = summoner.league_entries.fives  # For solo/duo queue
        if rank_info:
            st.write(f"**Rank:** {rank_info.tier} {rank_info.division} ({rank_info.league_points} LP)")
        else:
            st.write("**Rank:** Unranked")
    except Exception as e:
        st.error(f"Error: {e}")
'''