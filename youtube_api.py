from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from preprocessing.objects import video
from preprocessing.objects import query

# Calls Youtube API and retrieves transcript
def youtube_request(query, link =''):
    try:
        load_dotenv()
        youtube = build('youtube', 'v3', developerKey=os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))

        if query.get_select():
            request_id = youtube.search().list(part='snippet', q=link, maxResults = query.get_max_results())
            response = request_ids.execute()
            print(response)

        else:
            request_ids = youtube.search().list(part='snippet', q=query.get_search(), maxResults = query.get_max_results(), type=query.get_type(), videoCaption='closedCaption')
            response = request_ids.execute()

        return response

    except:
        print('Error retrieving video information')

def transcript_request(url):
    try:
        srt = YouTubeTranscriptApi.get_transcript(url, languages=['en'])
        for text in srt:
            transcript = transcript + text['text'] + ' '

        return transcript

    except:
        print('Error retrieving transcript')

def run_youtube_query(query):

    # If manual selections made, retrieves transcript and specific video information from youtube API:
    if query.get_selection():
        for link in query.get_selection():
            response = youtube_request(query, link)
            for items in response['items']:
                new_video = video(items['id']['videoId'], items['snippet']['channelTitle'],'',items['snippet']['publishedAt'], items['snippet']['title'], transcript_request(link), '')
                query.add_video_object(new_video)

            return query

    # Calls Youtbue API if no manual selection made:
    else:
        query_response = youtube_request(query)
        # Iterates through JSON response and adds video object to query list
        try:
            for items in query_response['items']:
                new_video = video(items['id']['videoId'], items['snippet']['channelTitle'],'',items['snippet']['publishedAt'], items['snippet']['title'], transcript_request(items['id']['videoId'], ''))
                query.add_video_object(new_video)
        except:
            print("Error creating video object")

    return query