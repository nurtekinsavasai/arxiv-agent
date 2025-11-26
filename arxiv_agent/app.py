import streamlit as st

st.set_page_config(page_title="Redirecting")

st.markdown(
    """
    <script>
        window.location.replace("https://research-aiagent.streamlit.app/");
    </script>
    """,
    unsafe_allow_html=True,
)

st.write("Redirecting to the new version of the app...")
