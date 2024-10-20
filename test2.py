from dotenv import load_dotenv
import os
import googleapiclient.discovery
import googleapiclient.errors
import json


def configure():
    load_dotenv()


configure()

api_service_name = "youtube"
api_version = 'v3'
DEVELOPER_KEY = os.getenv("api_key")

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)


def req(token=None):
    if token:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId="ZfUf-lcvCCs",
            maxResults=100,
            pageToken=token
        )
    else:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId="ZfUf-lcvCCs",
            maxResults=100,
        )

    response = request.execute()

    return response


response = req()

n = 1

for item in response['items']:
    print(n)
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
    print()
    n += 1

pageToken = response['nextPageToken']
print(pageToken)
req(pageToken)

for item in response['items']:
    print(n)
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
    print()
    n += 1

