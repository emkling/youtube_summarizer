from preprocessing.objects import query
from generate_summary import generate

def run():

    # What to search for
    search_field = 'What is the future of AI'

    # What to ask ChatGPT
    request = "Produce a detailed, bullet-pointed, organized summary of the following youtube transcripts: " 

    # Use Youtube API or local transcription with OpenAI Whisper
    youtube_api = False
    
    # Manual selection of videos. Leave empty to use search results
    selection_queue = []

    # How many results you want queried
    max_results = 1

    # Search parameters
    type = 'video'
    upload_date = 'all_time'
    duration = 'any'
    sort_by = 'relevance'
    language = 'en'

    # Begins generation
    generate(query(search_field, max_results, youtube_api, request, type, upload_date, duration, sort_by, language, '', selection_queue))
    
if __name__ == '__main__':
    run()