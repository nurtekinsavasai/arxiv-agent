import streamlit as st

# Setup page
st.set_page_config(page_title="We have moved!", layout="centered")

# The new URL
new_url = "https://research-aiagent.streamlit.app/"

# --- UI ---
st.title("📍 We have moved!")

st.warning("This version of the app is discontinued.")

st.write("We have moved to a new URL. Please use the button below to access the latest version:")

# 1. The Big Button (Primary Action)
st.link_button("Go to New App", new_url, type="primary")

# 2. Text Link (Backup)
st.markdown(f"Or click here: [{new_url}]({new_url})")
