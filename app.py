import os
from googleapiclient.discovery import build
import streamlit as st

# ✅ Render ke Environment Variable se API key lene ke liye os.environ use karein
API_KEY = os.environ.get("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=API_KEY)

def search_videos(query):
    req = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=10,
        type="video"
    )
    res = req.execute()
    videos = []
    for item in res.get("items", []):
        vids = {
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "videoId": item["id"]["videoId"]
        }
        videos.append(vids)
    return videos

st.title("TypeBeatTool 🎧")
query = st.text_input("Enter Type Beat keyword (e.g., Drake Type Beat)")
if st.button("Search"):
    if query:
        videos = search_videos(query + " type beat")
        for vid in videos:
            st.write(f"**{vid['title']}** by *{vid['channel']}*")
            st.write(f"https://youtu.be/{vid['videoId']}")

