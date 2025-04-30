import streamlit as st
# import pandas as pd
# import numpy as np
# import requests
# import psycopg2

# connection = psycopg2.connect(host=cocnfig.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB+PASS)

# Define the pages
Page_1 = st.Page("Page1_performance.py" , title="P.1 - Performance")
page_2 = st.Page("page2_screener.py"    , title="P.2 - Stock Screener")
page_3 = st.Page("page3_datasets.py"    , title="P.3 - Update Datasets")

# Set up navigation
pg = st.navigation([Page_1, page_2, page_3])

# Run the selected page
pg.run()