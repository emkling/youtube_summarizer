import whisper
from pytube import YouTube
from pyannote.audio import Pipeline

# Converts URL from youtube to mp4 file for OpenAI Whisper compatability
def convert_to_mp4(url, filename):
    print('URL imported: ' + url)
    destination = "C:\\Users\\broth\\OneDrive\\Desktop\\Programs\\Youtube Summarizer\\preprocessing\\audio_files"
    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download(output_path=destination, filename=filename + '.mp4')

# Transcribes local mp4 file to text
def transcribe_all_files(file_name):
    directory_path = 'Youtube Summarizer/preprocessing/audio_files/'
    model = whisper.load_model('tiny') # smallest model for faster run time
    result = model.transcribe(directory_path + str(file_name), fp16=False)
    print('Transcription complete')

    return result['text']

def diarization(file_name):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1")
    diarization = pipeline(file_name)

    with open('audio.rttm','w') as rttm:
        rttm.write(diarization.to_rttm())

    

