import streamlit as st
import yt_dlp
import os

def download_video(url, filename):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{filename}.%(ext)s',
        'noplaylist': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        },
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

st.title("ANY Video Downloader")

video_url = st.text_input("Enter the video URL:")
custom_filename = st.text_input("Enter the desired filename (without extension):")

if st.button("Download Video"):
    if video_url and custom_filename:
        st.info("Downloading... Please wait.")
        try:
            download_video(video_url, custom_filename)
            st.success(f"Download Complete! Video saved as '{custom_filename}'")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter both a valid URL and a filename.")
