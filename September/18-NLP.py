import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk import pos_tag, ngrams
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Download resources if not present
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

st.title("📝 NLP Playground with Streamlit")

# User text input
user_text = st.text_area("Enter your text here:")

# Sidebar options
st.sidebar.header("Options")

# Tokenization
do_tokenize = st.sidebar.checkbox("Tokenize Text", value=True)

# N-grams
ngram_choice = st.sidebar.radio("Choose N-gram", ("Unigram", "Bigram", "Trigram", "Custom"))
if ngram_choice == "Custom":
    n_val = st.sidebar.slider("Select N", 2, 6, 2)

# Stopwords
remove_stop = st.sidebar.checkbox("Remove Stopwords")

# Stemming
stemmer_option = st.sidebar.selectbox("Choose Stemmer", ("None", "Porter", "Lancaster", "Snowball"))

# Lemmatization
lemmatize_option = st.sidebar.checkbox("Apply Lemmatization")

# POS tagging
pos_option = st.sidebar.checkbox("POS Tagging")

# Word cloud
wordcloud_option = st.sidebar.checkbox("Generate Word Cloud")


if st.button("Process Text"):
    if user_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Tokenization
        if do_tokenize:
            tokens = word_tokenize(user_text)
        else:
            tokens = user_text.split()

        # Stopword removal
        if remove_stop:
            stop_words = set(stopwords.words('english'))
            tokens = [t for t in tokens if t.lower() not in stop_words]

        # Stemming
        if stemmer_option != "None":
            if stemmer_option == "Porter":
                stemmer = PorterStemmer()
            elif stemmer_option == "Lancaster":
                stemmer = LancasterStemmer()
            elif stemmer_option == "Snowball":
                stemmer = SnowballStemmer("english")
            tokens = [stemmer.stem(t) for t in tokens]

        # Lemmatization
        if lemmatize_option:
            lemmatizer = WordNetLemmatizer()
            tokens = [lemmatizer.lemmatize(t) for t in tokens]

        # N-grams
        if ngram_choice == "Unigram":
            output_tokens = tokens
        elif ngram_choice == "Bigram":
            output_tokens = list(ngrams(tokens, 2))
        elif ngram_choice == "Trigram":
            output_tokens = list(ngrams(tokens, 3))
        else:
            output_tokens = list(ngrams(tokens, n_val))

        st.subheader("Processed Output")
        st.write(output_tokens)

        # POS tagging
        if pos_option:
            st.subheader("POS Tags")
            st.write(pos_tag(tokens))

        # Word Cloud
        if wordcloud_option:
            st.subheader("Word Cloud")
            text_for_wc = " ".join(tokens)
            wc = WordCloud(width=800, height=400, background_color='white').generate(text_for_wc)
            fig, ax = plt.subplots()
            ax.imshow(wc, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
