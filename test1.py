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

request = youtube.commentThreads().list(
    part="snippet",
    videoId="ZfUf-lcvCCs",
    maxResults=400
)
response = request.execute()

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)

n = 1
for item in response['items']:
    print(n)
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
    print()
    n += 1

