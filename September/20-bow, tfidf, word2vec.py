import nltk

paragraph =  """I have three visions for India. In 3000 years of our history, people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture, their history and tried to enforce our way of life on them. Why? Because we respect the freedom of others.That is why my first vision is that of freedom. I believe that India got its first vision of this in 1857, when we started the War of Independence. It is this freedom thatwe must protect and nurture and build on. If we are not free, no one will respect us.My second vision for India’s development. For fifty years we have been a developing nation.It is time we see ourselves as a developed nation. We are among the top 5 nations of the worldin terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.Our achievements are being globally recognised today. Yet we lack the self-confidence tosee ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?I have a third vision. India must stand up to the world. Because I believe that unless India stands up to the world, no one will respect us. Only strength respects strength. We must be strong not only as a military power but also as an economic power. Both must go hand-in-hand. My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. I see four milestones in my career"""

# cleaning
import re  #regular expression
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

from gensim.models import Word2Vec

ps = PorterStemmer()
wordnet = WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)

corpus = []

for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])     #Keeps only letters A–Z; removes numbers/punctuation.
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]      #Stopword Removal + Lemmatization
    review = ' '.join(review)               #Converts list of words back into a cleaned sentence string.
    corpus.append(review)                   #Stores processed sentences into a list (corpus).
    

# BOW 
from sklearn.feature_extraction.text import CountVectorizer       #Converts text into a matrix of word counts.
cv = CountVectorizer()
x_bow = cv.fit_transform(corpus).toarray()

# TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer       #Similar to BoW, but instead of raw counts, it weighs words based on importance
tf = TfidfVectorizer()
x_tf = tf.fit_transform(corpus).toarray()

#WORD2WEB

# text Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',paragraph)     #Uses regex substitution (re.sub) to remove reference numbers like [1], [23] from the text.
text = re.sub(r'\s+',' ',text)                 #Replaces multiple spaces / newlines (\s+) with a single space.
text = text.lower()
text = re.sub(r'\d',' ',text)                  #Removes all digits
text = re.sub(r'\s+',' ',text)                 #Again replaces extra spaces with a single space (cleanup after digit removal).

sentences = nltk.sent_tokenize(text)            #Splits the cleaned text into sentences.
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]        #Splits each sentence into words (tokens).

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]   #Loops through each sentence and removes stopwords
    

model = Word2Vec(sentences, min_count=1)        #Trains a Word2Vec model on your dataset (sentences).
words = model.wv.key_to_index

vector = model.wv['war']                        #Fetches the word embedding (a dense numeric vector) for "war"

similar = model.wv.most_similar('war')          #Finds words that are most similar to "war", using cosine similarity between word vectors.
similar = model.wv.most_similar('freedom')
similar = model.wv.most_similar('vikram')
similar = model.wv.most_similar('son')