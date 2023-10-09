# import os
# import google.oauth2.credentials
# import google_auth_oauthlib.flow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from google_auth_oauthlib.flow import InstalledAppFlow


# SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']
# API_SERVICE_NAME = 'youtubeAnalytics'
# API_VERSION = 'v2'
# CLIENT_SECRETS_FILE = '/Users/zhenglongwu/Documents/GitHub/MSIN0006/Lab 1 Project/data/client_secret_645307431836-n4p9lb9hpa7g0ghekiqh1681p5b4msrh.apps.googleusercontent.com.json'


# def get_service():
#    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
#    credentials = flow.run
#    return build(API_SERVICE_NAME, 
#                 API_VERSION, 
#                 credentials=credentials)


# def execute_api_request(client_library_function, **kwargs):
#    response = client_library_function(**kwargs).execute()
#    print(response)

# def get():
   
#    youtubeAnalytics = get_service()
#    execute_api_request(youtubeAnalytics.reports().query,
#                        ids='channel==UCBOIxRfSIXDT03e116VTzCw',
#                        startDate='2017-01-01',
#                        endDate='2018-01-01',
#                        metrics='views,likes')
   

# get()