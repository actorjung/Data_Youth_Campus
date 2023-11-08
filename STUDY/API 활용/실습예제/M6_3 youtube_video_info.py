import requests
import pandas as pd
import datetime
import sqlite3
import logging

api_key = 'AIzaSyDL8EkpvA7VqSsbaSdlC37N3aLSclp-uB0'
headers = {'Accept': 'application/json'}

logger = logging.getLogger('m6_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s')
file_handler = logging.FileHandler('c:/python_class/m6_logs/youtube_video_info.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_channel_video_list():
    # 금융위원회 유튜브 채널
    channel_id = 'UCuJz-PXNMdWQr6TNM4htENw'
    params = {
            "key": api_key,
            "part": "id,contentDetails",
            "channelId": channel_id,
            "maxResults": 50,
            "fields": "nextPageToken,pageInfo,items(contentDetails/upload)"
    }
    url = 'https://www.googleapis.com/youtube/v3/activities'
    res = requests.get(url, headers=headers, params=params)
    
    # 동영상 목록을 리스트로 저장
    video_list = []
    for video in res.json()['items']:
        video_id = video['contentDetails']['upload']['videoId']
        video_list.append(video_id)
        
    return video_list


def get_video_info(video_list):
    now = datetime.datetime.now()
    params = {
        # api키 항상 먼저 입력
        "key": api_key,
        # 비디오 목록을 콤마(,)로 묶어 한줄의 텍스트로 만듬
        "id": ",".join(video_list),
        "part": 'id, snippet, statistics'
    }
    url = 'https://www.googleapis.com/youtube/v3/videos'
    res = requests.get(url, headers=headers, params=params)

    df = pd.DataFrame()
    for video in res.json()['items']:
        save_params = {}
        video_id = video['id']
        save_params.update({'_id': video_id, '_date': now.date(), '_hour': now.hour, '_min': now.minute})
        save_params.update(video['statistics'])
        df = df.append(save_params, ignore_index=True)

    # viewCount가 TEXT이기 때문에 제대로 정렬되지 않음
    df['viewCount'] = df['viewCount'].astype(int)
    df = df.sort_values(by='viewCount', ascending=True)
    
    return df


def save_to_file(video_info):
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d_%H_%M')
    file_name = f"c:/python_class/m6_files/youtube_video_info_{now_str}.csv"
    video_info.to_csv(file_name, encoding='utf-8-sig', index=False)
    
    
def save_to_db(video_info):
    conn = sqlite3.connect('c:/python_class/hello_db.db')
    video_info.to_sql('youtube_video_info', conn, index=False, if_exists='append')
    conn.close()

try:
    video_list = get_channel_video_list()
    video_info = get_video_info(video_list)
    save_to_file(video_info)
    save_to_db(video_info)
    logger.info('success')
except Exception as e:
    logger.error(str(e))