from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from preprocessing.objects import video
from preprocessing.objects import query
from preprocessing.transcribe_audio import transcribe_all_files
from preprocessing.transcribe_audio import convert_to_mp4

# This file only is used when user wants to web scrape videos from youtube, and then manually transcribe with OpenAI Whisper

# Option for leaving browser open after commands executed
options = Options()
options.add_experimental_option('detach', True)

# Option for disabling infobar at the top of the browser
options.add_argument('disable_infobars')

# Selenium drivers for Chrome
s=Service(ChromeDriverManager().install())
website = 'https://www.youtube.com/results?search_query='
driver = webdriver.Chrome(service=s, options=options)

def set_query(search_field):
    return website + search_field + '&sp=EgIYAw%253D%253D'

# Continously scrolls browser to bottom of page until enough videos are loaded to be scraped
def scroll_to_bottom(count):
    count_satisfied = False

    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while count_satisfied == False:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        # Wait to load page
        time.sleep(10)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        title_count = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
        current_count = 0

        for object in title_count:
            if object.get_attribute('href'):
                current_count += 1
                print(current_count)

                if current_count >= count:
                    count_satisfied = True
                    break

# Query function for web scraping
def run_query(count, current_query):

    # Retrieves relevant elements
    driver.implicitly_wait(10)
    titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
    views = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')
    channel = driver.find_elements(By.XPATH, '//*[@id="text"]/a')
    date_published = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[2]')
    #duration = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-thumbnail-overlay-time-status-renderer')

    # Remove first ad element if present (Ads do not have views or dates, hence only need to pop first elements of titles and channels)
    if driver.find_elements(By.XPATH, '//*[@id="ad-badge-container"]/ytd-badge-supported-renderer/div/span'):
        titles.pop(0)
        channel.pop(0)

    # Counts how many links have been stored    
    link_count = 0

    for a, b, c, d, in zip(titles, views, channel, date_published):
        if a.get_attribute('href'):
            link_count += 1
            channel_name = str(c.get_attribute('href'))
            split = channel_name.find('@')
            
            # New video object with paramenters: link, channel, views, date, title, summary, audio_file
            new_video = video(str(a.get_attribute('href')), channel_name, b.text, d.text, a.text, '', 'File' + str(link_count) + '.mp4')
            print(new_video.get_video())
            
            # Converts and stores video to mp4 file
            convert_to_mp4(a.get_attribute('href'), 'File' + str(link_count))
            
            # Transcribes the audio file
            new_video.set_summary(transcribe_all_files('File' + str(link_count) + '.mp4'))

            # Stores video object in query object
            current_query.add_video_object(new_video)

            print(new_video.get_summary())

        # Once enough links have been stored, breaks loop
        if link_count >= count:
            break

    return current_query

# Main function for retrieving videos
def retrieve(query):

    # Ensures that manual selection has not been made before running query
    if len(query.get_selection()) == 0 :
        driver.get(set_query(query.get_search()))
        scroll_to_bottom(query.get_max_results())
        return_query = run_query(query.get_max_results(), query)

    driver.quit()

    return return_query

