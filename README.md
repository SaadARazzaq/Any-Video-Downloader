# Any Video Downloader (Streamlit + yt-dlp)

## Overview
This is a simple web application built using **Streamlit** and **yt-dlp** that allows users to download videos by providing a video URL.

## Features
- User-friendly **web interface** with Streamlit
- Supports **downloading videos** in the best available quality
- **No playlist downloads** (single video only)
- **Real-time status updates** during the download process

## Installation

### Prerequisites
Make sure you have **Python 3.7+** installed on your system.

### Steps to Install
```sh
# Clone this repository
git clone https://github.com/saadarazzaq/Any-Video-Downloader.git
cd youtube-video-downloader

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
```sh
# Run the Streamlit app
streamlit run app.py
```

1. Open the **URL displayed in the terminal** (usually `http://localhost:8501`).
2. Enter a **YouTube video URL** and click **Download Video**.
3. The video will be downloaded to the current directory.

## Project Structure
```sh
/project dir
│── app.py             # Streamlit UI for YouTube video download
│── requirements.txt   # Dependencies list
│── README.md          # Project documentation
```

## Dependencies
The project uses:
- `streamlit` - To create the web-based UI
- `yt-dlp` - For downloading YouTube videos

## Troubleshooting
- If the video doesn't download, check if `yt-dlp` is updated:
  ```sh
  pip install --upgrade yt-dlp
  ```
- Make sure the **YouTube URL** is correct and publicly accessible.
- If Streamlit UI does not open, manually go to `http://localhost:8501` in your browser.

## License
This project is licensed under the **MIT License**. Feel free to modify and share.

## Contributing
Pull requests are welcome! Please follow standard coding practices and ensure code quality before submitting.

---
### Author
[💖 Saad Abdur Razzaq](https://github.com/saadarazzaq)

