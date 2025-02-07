import streamlit as st

st.set_page_config(
    page_title="Leaderboard",
    page_icon="🏆",
    initial_sidebar_state="collapsed",
    menu_items={
        'Report a bug': "mailto:nick.vanoosterwyck@uantwerpen.be",
        'About': "Crafted with ❤️ by the Cosys-Lab team"
    }
)

# Sidebar
st.logo(
    "Assets/Logos/cosys-en-neg-rgb.svg",
    icon_image="Assets/Logos/cosys-en-neg-rgb-icon.svg",
    size='large',
    link='https://www.uantwerpen.be/en/research-groups/cosys-lab/'
)
st.sidebar.title('Cosys-Lab King of the Kicker 👑')

# Page Content
#st.title('Cosys-Lab King of the Kicker 👑')
st.header('🏆 Leaderboard')
leaderboard = st.empty()
st.divider()

# Initialize the players
if 'players' not in st.session_state:
    st.session_state.players = {
        'Nick': 0,
        'Kiran': 0,
        'Santi': 0,
        'Brejt': 0,
        'Baptist': 0,
        'Aris': 0
    }

# Initialize the matches
if 'matches' not in st.session_state:
    st.session_state.matches = []

def update_leaderboard():
    sorted_players = sorted(st.session_state.players.items(), key=lambda x: x[1], reverse=True)
    leaderboard_data = [{'Player': player, 'Score': score} for player, score in sorted_players]
    leaderboard.table(leaderboard_data)

update_leaderboard()

# Add a Game
if 'ADDGAME_expanded' not in st.session_state:
    st.session_state.ADDGAME_expanded = False

with st.expander("⚽ Add a Game", expanded=st.session_state.ADDGAME_expanded) as expander:
    col1, col2 = st.columns(2)
    with col1:
        winner1 = st.selectbox('Select the first winner', list(st.session_state.players.keys()), index=0)
        winner2 = st.selectbox('Select the second winner', list(st.session_state.players.keys()), index=1)
    with col2:
        loser1 = st.selectbox('Select the first loser', list(st.session_state.players.keys()), index=2)
        loser2 = st.selectbox('Select the second loser', list(st.session_state.players.keys()), index=3)

    if st.button('Confirm'):
        if len(set([winner1, winner2, loser1, loser2])) == 4:
            st.session_state.players[winner1] += 1
            st.session_state.players[winner2] += 1
            st.session_state.players[loser1] -= 1
            st.session_state.players[loser2] -= 1
            st.session_state.matches.append((winner1, winner2, loser1, loser2))
            update_leaderboard()
            st.session_state.ADDGAME_expanded = True
            st.rerun()
        else:
            st.error('All players must be unique')

st.write(st.session_state.ADDGAME_expanded)
with st.expander("Test", expanded=st.session_state.ADDGAME_expanded) as expander2:
    col1, col2 = st.columns(2)