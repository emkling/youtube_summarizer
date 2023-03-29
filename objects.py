class query:
    def __init__(self, search, max_results=1, youtube_api = False, request = '', type = 'video', upload_date = '', duration ='', sort_by = 'relevance', language = 'en', master_summary = '', selection = []):
        self.search = search
        self.max_results = max_results
        self.youtube_api = youtube_api
        self.request = request
        self.type = type
        self.upload_date = upload_date
        self.duration = duration
        self.sort_by = sort_by
        self.videos = []
        self.video_links = []
        self.video_objects = []
        self.video_summaries = []
        self.selection = selection
        self.master_summary = master_summary
        self.language = language

    # Add Functions
    def add_video(self, video):
        self.videos.append(video)

    def add_video_link(self, video_link):
        self.video_links.append(video_link)

    def add_video_object(self, video_object):
        self.video_objects.append(video_object)

    def add_video_summary(self, video_summary):
        self.video_summaries.append(video_summary)

    # Getter Functions
    def get_search(self):
        return self.search

    def get_max_results(self):
        return self.max_results

    def get_type(self):
        return self.type

    def get_upload_date(self):
        return self.upload_date

    def get_duration(self):
        return self.duration

    def get_sort_by(self):
        return self.sort_by

    def get_videos(self):
        return self.videos

    def get_video_links(self):
        return self.video_links

    def get_video_objects(self):
        return self.video_objects

    def get_video_summaries(self):
        return self.video_summaries

    def get_language(self):
        return self.language
    
    def get_master_summary(self):
        return self.master_summary

    def get_manual_select(self):
        return self.manual_select
    
    def get_youtube_api(self):
        return self.youtube_api

    def get_request(self):
        return self.request

    def get_selection(self):
        return self.selection

    # All Setter Functions
    def set_query(self, search):
        self.search = search

    def set_max_results(self, max_results):
        self.max_results = max_results

    def set_type(self, type):
        self.type = type

    def set_upload_date(self, upload_date):
        self.upload_date = upload_date

    def set_duration(self, duration):
        self.duration = duration

    def set_sort_by(self, sort_by):
        self.sort_by = sort_by

    def set_videos(self, videos):
        self.videos = videos
    
    def set_video_links(self, video_links):
        self.video_links = video_links

    def set_video_objects(self, video_objects):
        self.video_objects = video_objects

    def set_video_summaries(self, video_summaries):
        self.video_summaries = video_summaries

    def set_language(self, language):
        self.language = language
        
    def set_master_summary(self, master_summary):
        self.master_summary = master_summary
    
    def set_manual_select(self, manual_select):
        self.manual_select = manual_select

    def set_selection(self, selection):
        self.selection = selection

class video:
    def __init__(self, link='', creator ='', view_count='', upload_date='', title='', summary='', file=''):
        self.link = link
        self.creator = creator
        self.view_count = view_count
        self.upload_date = upload_date
        self.title = title
        self.summary = summary
        self.file = file

# Getter Functions
    def get_video(self):
        return (self.link, self.creator, self.view_count, self.upload_date, self.title, self.summary, self.file)

    def get_link(self):
        return self.link
    
    def get_creator(self):
        return self.creator
    
    def get_view_count(self):
        return self.view_count

    def get_upload_date(self):
        return self.upload_date

    def get_title(self):
        return self.title

    def get_summary(self):
        return self.summary

    def get_file(self):
        return self.file

# All Setter Functions
    def set_link(self, link):
        self.link = link

    def set_creator(self, creator):
        self.creator = creator

    def set_view_count(self, view_count):
        self.view_count = view_count

    def set_upload_date(self, upload_date):
        self.upload_date = upload_date

    def set_title(self, title):
        self.title = title
    
    def set_summary(self, summary):
        self.summary = summary

    def set_file(self, file):
        self.file = file

