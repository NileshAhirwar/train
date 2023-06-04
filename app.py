import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    initial_sidebar_state="collapsed"
)

st.write("❤️Welocom To AI Assited Training Material Creation!❤️")


st.markdown(
    """
    Go to : 
    - <a href="Trainer" target="_blank">Trainer Page</a>
    - <a href="Trainee">Trainee Page</a>
    """,
    unsafe_allow_html=True
)
