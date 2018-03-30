# http://textblob.readthedocs.io/en/dev/install.html
# pip install nltk, textblob
# python -m textblob.download_corpora lite

import pickle
import nltk
from textblob import TextBlob
import time

message = str(pickle.load( open( "message.p", "rb" ) ))

message_sentiment = TextBlob(message).sentiment.polarity

if message_sentiment < -0.2:

    message_response = "bad"

elif -0.2 <= message_sentiment <= 0.4:

    message_response = "okay"

else:

    message_response = "good"

pickle.dump(message_response, open( "sentiment.p", "wb" ), protocol=2 )