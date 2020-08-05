#! /usr/bin/python

import requests
from bs4 import BeautifulSoup
import lxml
from googleapiclient.discovery import build

def scrape_wikipedia_tables(url):
    '''Returns the table html objects from a wikipedia page'''
    page = requests.get(url)

    # Parse the HTML from URL
    # From docstirng --> recommended to name a specific parser
    soup = BeautifulSoup(page.text, 'lxml')

    # Find all tables in HTML
    all_tables = soup.find_all("table")
    print(f'# of Tables Found: {len(all_tables)}\n')
    return all_tables



# Define function to get statistics from each video
# From: Python Social Media Analytics, pg. 133
def get_statistics(video_id, api_key):
    '''Returns a JSON object with the statistics for a YouTube video'''
    url = 'https://www.googleapis.com/youtube/v3/videos'
    pms = {'key':api_key,
           'id':video_id,
           'part':'contentDetails,statistics'}
    res = requests.get(url, pms)
    data = res.json()
    return data




# From: https://gist.github.com/Evolution0/6f2a7f36aa27fe3a6ae61b1ec6a37740
# Define function to paginate through a specific YouTube channel
def fetch_all_youtube_videos(channel_id, api_key):
    youtube = build("youtube", "v3", developerKey=api_key)
    res = youtube.search().list(
        part="snippet",
        type="video",
        channelId=channel_id,
        maxResults="50"
    ).execute()

    next_page_token = res['nextPageToken']
    while 'nextPageToken' in res:
        next_page = youtube.search().list(
            part="snippet",
            type="video",
            channelId=channel_id,
            maxResults="50",
            pageToken=next_page_token
        ).execute()
        res['items'] = res['items'] + next_page['items']

        if 'nextPageToken' not in next_page:
            res.pop('nextPageToken', None)
        else:
            next_page_token = next_page['nextPageToken']
    return res


import os
import youtube_dl

def download_youtube_video_mp3(url, filename):
    '''Download a YouTube video to target directory'''
    if not os.path.exists('../audio'):
        os.mkdir('../audio')
    
    ydl_opts = {
        'outtmpl': f'audio/{filename}.mp3',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return True