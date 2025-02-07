import streamlit as st

# Sidebar
st.logo("Assets/Logos/cosys-en-neg-rgb.svg", icon_image="Assets/Logos/cosys-en-neg-rgb-icon.svg")
st.sidebar.text("Nick Van Oosterwyck")

# Main Title
st.title('Cosys-Lab King of the Kicker 👑')

# Leaderboard
st.header('🏆 Leaderboard ')
players = {'Nick': 0, 'Kiran': 0, 'Santi': 0}
leaderboard = st.empty()
matches = []

def update_leaderboard():
    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
    leaderboard_data = [{'Player': player, 'Score': score} for player, score in sorted_players]
    leaderboard.table(leaderboard_data)

update_leaderboard()

st.divider()

# Add a Game
st.header('⚽ Add a Game')
winner = st.selectbox('Select the winner', list(players.keys()),index=1)
loser = st.selectbox('Select the loser', list(players.keys()),index=2)

if st.button('Confirm'):
    if winner != loser:
        players[winner] += 1
        players[loser] -= 1
        matches.append((winner, loser))
        update_leaderboard()
    else:
        st.error('Winner and loser cannot be the same player')

st.divider()

if st.button('See Matches'):
    st.header('See Matches')
    if matches:
        match_table = [{'Winner': match[0], 'Loser': match[1]} for match in matches]
        st.table(match_table)
    else:
        st.write('No matches played yet.')