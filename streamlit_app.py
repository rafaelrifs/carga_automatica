# Terminal -> pip install st-gsheets-connection

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/15UJIu0EvQWl2WD8rPMhxgnObFbZv9_wCHNuHC5RMrPs/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1], ttl=6)

st.dataframe(data)
