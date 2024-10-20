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


def req():
    request = youtube.commentThreads().list(
        part="snippet",
        videoId="ZfUf-lcvCCs",
        maxResults=4000,
    )

    response = request.execute()

    return response


def more_req(token):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId="ZfUf-lcvCCs",
        maxResults=100,
        pageToken=token
    )

    response = request.execute()

    return response


response = req()

comments = []

n = 1
while True:

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
        print(n)
        print(comment)
        print()
        n += 1

    next_page_token = response.get('nextPageToken')
    print(next_page_token)

    if next_page_token:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId="ZfUf-lcvCCs",
            maxResults=100,
            pageToken=next_page_token
        )
        response = request.execute()

    else:
        print("\n\n\n\n\n")
        print("No more pages available")
        break

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(comments, f, ensure_ascii=False, indent=4)

