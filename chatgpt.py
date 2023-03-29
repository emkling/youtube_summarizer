from preprocessing.objects import video
from preprocessing.objects import query
from pyChatGPT import ChatGPT
import os
from dotenv import load_dotenv

def chat_gpt(query):
    load_dotenv()
    api = ChatGPT(os.getenv('chat_gpt_token'))
    open = True

    try:
        master_request = "Based on the following accumulated summaries, what computer is considered the best: "
        for video in query.get_video_objects():
            try:
                summary = video.get_summary()
                split_number = int(len(summary) / 490)
                if split_number > 1: 
                    for i in range(split_number):
                        resp = api.send_message(query.get_search() + summary[i*490:(i+1)*490])
                        print('\n' + resp['message'] + '\n')
                else:
                    print(video.get_title()) 
                    resp = api.send_message(query.get_search()+ ': ' + summary)
                    print('\n' + resp['message'] + '\n')
                    master_request = master_request + resp['message'] + " "
            except:
                print('Too long of input')
                continue

        master_response = api.send_message(master_request)
        print('\nMaster Request: \n')
        print('\n' + master_response['message'] + '\n')
    except Exception as e: print(e)
    while open:
        convo = input('')
        if convo == 'q':
            open = False
        else:
            resp = api.send_message(convo)
            print('\n' + resp['message'] + '\n')
        
    #api.refresh_auth()
    #api.reset_conversation()