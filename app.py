import streamlit as st

st.title("🏏 IPL Match Outcome Predictor")
st.markdown("Predict match results using toss, venue & team insights")

teams = ["MI", "CSK", "RCB", "KKR"]

team1 = st.selectbox("Select Team 1", teams)
team2 = st.selectbox("Select Team 2", teams)
toss = st.selectbox("Toss Winner", [team1, team2])
venue = st.selectbox("Venue", ["Mumbai", "Chennai", "Bangalore", "Kolkata"])

# same team check
if team1 == team2:
    st.error("❌ Please select different teams")

# prediction
if st.button("Predict Winner"):

    if team1 == team2:
        st.stop()

    if venue == "Mumbai" and team1 == "MI":
        winner = team1
    elif venue == "Chennai" and team1 == "CSK":
        winner = team1
    elif toss == team1:
        winner = team1
    else:
        winner = team2

    st.markdown(f"## 🏆 Winner: **{winner}**")

st.caption("⚡ Based on simple heuristic model (toss + venue advantage)")