import streamlit as st
import streamlit.components.v1 as components

'''
st.set_page_config(page_title="Redirecting...")

# The new URL
new_url = "https://research-aiagent.streamlit.app/"

st.markdown(
    f'<meta http-equiv="refresh" content="0;url={new_url}">',
    unsafe_allow_html=True
)

# Method 3: Visual Fallback (User Click)
st.title("We have moved!")
st.info("You are being redirected to the new version of the app...")
st.markdown(f"If you are not redirected automatically, [click here]({new_url}).")
st.link_button("Go to New App", new_url, type="primary")
'''

# 1. Setup Page
st.set_page_config(page_title="Redirecting...", layout="centered")

# The new URL
new_url = "https://research-aiagent.streamlit.app/"

# =========================================================
# STRATEGY 2: The Component Iframe Script (Executes in Sandbox)
# =========================================================
# This creates a tiny invisible iframe that runs pure JS.
# We try both window.parent and window.top to escape the sandbox.
js_code = f"""
<script>
    try {{
        window.top.location.href = "{new_url}";
    }} catch (e) {{
        window.parent.location.href = "{new_url}";
    }}
</script>
"""
components.html(js_code, height=0, width=0)