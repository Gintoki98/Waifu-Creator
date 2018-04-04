# http://textblob.readthedocs.io/en/dev/install.html
# pip install nltk, textblob
# python -m textblob.download_corpora lite

import nltk
from textblob import TextBlob
import sys

message = " ".join(sys.argv[1:])
message_sentiment = TextBlob(message).sentiment.polarity

if message_sentiment < -0.2:

    message_response = "bad"

elif -0.2 <= message_sentiment <= 0.4:

    message_response = "okay"

else:

    message_response = "good"

print(message_response)
