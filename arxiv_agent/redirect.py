import streamlit as st

st.set_page_config(page_title="Redirecting to Research Agent")

st.markdown(
    """
    <meta http-equiv="refresh" content="0; url='https://research-aiagent.streamlit.app/'" />
    """,
    unsafe_allow_html=True
)

st.write("Redirecting…")

