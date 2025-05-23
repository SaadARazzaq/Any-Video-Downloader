import streamlit as st
import yt_dlp
import os
import tempfile
import re

def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9-_ ]', '', filename).strip()

def download_video(url):
    temp_dir = tempfile.gettempdir()


    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        sanitized_title = sanitize_filename(info['title'])
        video_path = os.path.join(temp_dir, f"{sanitized_title}.{info['ext']}")


        if os.path.exists(video_path):
            return video_path


    ydl_opts = {
        'format': 'best', 
        'outtmpl': video_path, 
        'noplaylist': True,  
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        },
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return video_path


st.title("~ ANY Video Downloader (This does not support carousels ❌)")

video_url = st.text_input("Enter the video URL:")

if st.button("Download Video"):
    if video_url:
        st.info("Downloading... Please wait.")
        try:
            video_path = download_video(video_url)
            st.success("Download Complete! Click below (👇) to save the file.")

            # Provide the download link to the user
            with open(video_path, "rb") as file:
                st.download_button(
                    label="Download Video",
                    data=file,
                    file_name=os.path.basename(video_path),
                    mime="video/mp4"
                )
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL.")
