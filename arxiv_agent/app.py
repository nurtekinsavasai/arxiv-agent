import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Redirecting...")

# The new URL
new_url = "https://research-aiagent.streamlit.app/"

# Method 1: JavaScript Redirect via Components
# We use 'window.top.location.href' to ensure we break out of the Streamlit iframe
components.html(
    f"""
    <script>
        window.top.location.href = "{new_url}";
    </script>
    """,
    height=0,
)

# Method 2: HTML Meta Refresh (Fallback)
st.markdown(
    f'<meta http-equiv="refresh" content="0;url={new_url}">',
    unsafe_allow_html=True
)

# Method 3: Visual Fallback (User Click)
st.title("We have moved!")
st.info("You are being redirected to the new version of the app...")
st.markdown(f"If you are not redirected automatically, [click here]({new_url}).")
st.link_button("Go to New App", new_url, type="primary")