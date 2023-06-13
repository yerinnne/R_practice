import glob
import os
import sys
import csv
import pandas as pd
import numpy as np
import scipy as sp
from urllib.request import Request, urlopen
from urllib.parse import quote
import json
import requests
import math
import re
import numpy as np
import nltk
from nltk.tokenize import word_tokenize

def crawl_naver_blog(keywords):
    id = 'LCLES7mfCulkHetN_V9m'
    secret = 'GwtKq2nlAz'
    url = 'https://openapi.naver.com/v1/search/blog.json'
    headers = {'X-Naver-Client-Id':id, 'X-Naver-Client-Secret':secret}

    params = {
    'query' : keywords,
    'display' : 100,
    'start' : 1,
    'sort' : 'sim'} 
    
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        global a # 전역변수로 선언
        a = res.json().get('items')
        return a
    
    # 여러 키워드 크롤링
keywords = ['서울 숙소 추천','서울 맛집 추천','서울 액티비티 추천',
            '강원 숙소 추천', "강원 맛집 추천", '강원 액티비티 추천',
            '제주 숙소 추천', "제주 맛집 추천", '제주 액티비티 추천',
            '부산 숙소 추천', "부산 맛집 추천", '부산 액티비티 추천',
            '경기도 숙소 추천', "경기도 맛집 추천", '경기도 액티비티 추천']

#결과 리스트에 저장
key_list =[]
for keyword in keywords:
    key_list.append(crawl_naver_blog(keyword))

    import re
b=[]
for i in range(len(key_list)):
    # 특수문자를 제거한 모든 title
    a=[] 
    a=[key_list[i][j]['title'] for j in range(len(key_list[0]))]
    a=[re.sub(r"[^ㄱ-ㅣ가-힣\s]", "", j) for j in a] 

    # 특수문자를 제거한 모든 describtion
    c=[]
    c=[key_list[i][j]['description'] for j in range(len(key_list[0]))]
    c=[re.sub(r"[^ㄱ-ㅣ가-힣\s]", "", j) for j in c]

    d=a+c

    b.append(pd.DataFrame(d))

    df=pd.DataFrame()
df['서울숙소']=b[0]; df['서울맛집']=b[1]; df['서울관광']=b[2];
df['강원숙소']=b[3]; df['강원맛집']=b[4]; df['강원관광']=b[5]; 
df['제주숙소']=b[6]; df['제주맛집']=b[7]; df['제주관광']=b[8];
df['부산숙소']=b[9]; df['부산맛집']=b[10]; df['부산관광']=b[11];
df['경기숙소']=b[12]; df['경기맛집']=b[13]; df['경기관광']=b[14];