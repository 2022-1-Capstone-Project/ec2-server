import boto3
import sys
from boto3.session import Session
#! /usr/bin/env python

session = boto3.Session()
s3_client = session.client('s3')

BUCKET_NAME = 'fyp-music'

def handle_upload_wav(f):
#    s3_client = boto3.client('s3',
 #                           aws_access_key_id=AWS_ACCESS_KEY_ID,
  #                          aws_secret_access_key=AWS_ACCESS_SECRET_KEY)
    response = s3_client.upload_file(
            '/home/ubuntu/face-your-pace-function/fyp_download/result/'+f, BUCKET_NAME, 'music/'+ f.replace(" " , ""))

def handle_upload_mp3(f): # f = 파일명
#	s3_client = boto3.client('s3',
 #                           aws_access_key_id=ACCESS_KEY_ID,
  #                          aws_secret_access_key=ACCESS_SECRET_KEY)
	response = s3_client.upload_file(
            '/home/ubuntu/face-your-pace-function/fyp_download/result/'+f, BUCKET_NAME, 'music/'+ f.replace(" " , ""))
    # 로컬파일경로 + 파일명 + 파일종류, 버킷명, s3버킷의 원하는경로 + 파일명 + 파일종류

if __name__ == '__main__':
    f = sys.argv[1] 
    
    val = ".mp3" in f
    val2 = ".wav" in f

    if val:
        print("mp3 업로드 중")
        handle_upload_mp3(f)
        print("mp3 업로드 완료")
    else:
        print("wav 업로드 중")
        handle_upload_wav(f)
        print("wav 업로드 완료")
