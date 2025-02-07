import streamlit as st

st.header('📃 Matches')

# Matches
if st.session_state.matches:
    match_table = [{'Winner 1': match[0], 'Winner 2': match[1], 'Loser 1': match[2], 'Loser 2': match[3]} for match in st.session_state.matches]
    st.table(match_table)
else:
    st.write('No matches played yet.')