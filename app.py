import streamlit as st
import pandas as pd
import json
import glob
import os
from datetime import datetime

st.set_page_config(page_title="Gold Scripts Dashboard", layout="wide")
st.title("🔥 Top Gold Trading Scripts for Gold")

data_files = glob.glob("data/scripts_*.json")
if not data_files:
    st.error("No data yet. The scraper will run soon.")
    st.stop()

latest = max(data_files, key=os.path.getctime)
with open(latest) as f:
    scripts = json.load(f)

df = pd.DataFrame(scripts).sort_values('likes', ascending=False).head(10)
st.subheader("📊 Top 10 Most Liked Scripts")
st.dataframe(df[['script_name', 'author', 'likes']], use_container_width=True)
st.subheader("📈 Likes Distribution")
st.bar_chart(df.set_index('script_name')['likes'])
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
