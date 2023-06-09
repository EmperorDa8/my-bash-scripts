from textblob import TextBlob
from newspaper import Article
import nltk
from gtts import gTTS
from playsound import playsound
from pathlib import Path
import os
  


def speak(texts):
    """
        Convert the given text to speech and play the audio.
    
        Args:
            text (str): The text to convert to speech.
        """    
    tet=gTTS(text=texts, lang="en")
    filename="avoice.mp3"
    tet.save(filename)
    audio_path= Path().cwd() / "avoice.mp3"
    playsound(audio_path)
    os.remove(audio_path)

# URL of the article to analyze

url="https://punchng.com/meet-skitmaker-who-left-russia-for-nigeria-in-search-of-happiness/"


# Create an Article object and extract information from the URL

art=Article(url)
art.download()
art.parse()
art.nlp()


# Extract the summary text from the article
text_data=art.summary
#print(text_data)

# Analyze the sentiment of the text using TextBlob
blob=TextBlob(text_data)
sent= blob.sentiment.polarity
# Determine the sentiment and play the corresponding speech
if sent > 0:
    speak("quite positive!")
elif sent < 0 :
    speak("very negative!")
else:
    speak("fairly neutral")
    