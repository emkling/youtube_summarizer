from preprocessing.retrieve_videos import retrieve
from preprocessing.chatgpt import chat_gpt
from preprocessing.youtube_api import youtube_request
from preprocessing.objects import query


def generate(query_request):

    if query_request.get_youtube_api() == True:
        query_vidoes = youtube_request(query_request)
        chat_gpt(query_vidoes)
    else:
        query_vidoes = retrieve(query_request)
        chat_gpt(query_vidoes)

