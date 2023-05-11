# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13estrijFH9dYFjPza3C_VCgbaaic0D8K
"""

import pandas as pd

df = pd.read_csv('/content/NetFlix.csv')

df

print(list(df.columns))

df.shape

df.describe()

df.info()

df.duplicated().sum()

import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x = 'type' ,data =df)
plt.title('Movies Vs Tv Shows')
plt.figure(figsize=(20,8))

sns.set_palette('gist_ncar')
df.type.value_counts().plot(kind='pie',autopct='%1.0f%%',explode=(0.05,0.05))
plt.title('Distribution of type',fontsize=25,fontweight='bold')

plt.figure(figsize=(10,7))
sns.countplot(y=df['country'], order=df['country'].value_counts().index[0:20])
ax=plt.xticks(rotation = 0)

plt.figure(figsize=(20,10))
graph=sns.countplot(y='director',data=df,order=df.director.value_counts().head(10).index)
graph.set_title("top 10 Directors of Netflix",fontsize=15,fontweight='bold')

df['date_added']=pd.to_datetime(df['date_added'])
df['year_added']=df['date_added'].dt.year
df['month_added']=df['date_added'].dt.month

df.head(5)

df['year_added'].value_counts().reset_index().rename(columns={'index':'year','year_added':'movie_count'})

import plotly.express as px

graph=px.pie(df,names='year_added', height=500,width=900, hole=0.3, title='Netflix year distribution')
graph.show()

graph=px.pie(df,names='month_added', height=500,width=900, hole=0.3, title='Netflix month distribution')
graph.show()

plt.figure(figsize=(10,7))
ax=sns.countplot(y=df['rating'], order=df['rating'].value_counts().index[0:])

graph=px.pie(df,names='rating', height=500,width=900, hole=0.3, title='Netflix rating distribution')
graph.show()

!pip install wordcloud

from PIL import Image
from wordcloud import WordCloud, STOPWORDS

df_wc=df['title']
text=" ".join(i for i in df_wc)

stopwords=set(STOPWORDS)

wordcloud=WordCloud(stopwords=stopwords, background_color='white').generate(text)

plt.imshow(wordcloud,interpolation='nearest')
plt.axis('off')
plt.show()

"""preprocessing"""

from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

def Apply_stemming(text):
  text = [stemmer.stem(word) for word in text.split()]
  return " ".join(text)

df['description'] = df['description'].apply(Apply_stemming)
df.head()

from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer(max_features=8000,stop_words='english')

cv

df['tags']=df['description']+df['genres']

tags = df['tags']

tags

vector=cv.fit_transform(df['tags'].values.astype('U')).toarray()

vector.shape

"""cosine similarity"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.sentiment import SentimentIntensityAnalyzer

similarity = cosine_similarity(vector)

new_df = df.drop(columns=['description', 'genres'])

new_df

def recommend(tags): 
  index = df[df['title']==tags].index[0]
  recom = sorted(list(enumerate(similarity[index])),reverse=True, key=lambda vector:vector[1])
  for i in recom[0:10]:
    print(df.iloc[i[0]].title)

recommend("3 Heroines")

"""sentiment analysis"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.sentiment import SentimentIntensityAnalyzer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pandas as pd
import requests
from bs4 import BeautifulSoup

movie_reviews = []
url = 'https://www.google.com/search?q=movie+reviews+avengers+endgame'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for review in soup.find_all('div', {'class': 'b1hJbf'}):
    movie_reviews.append(review.get_text())

import nltk
from nltk.corpus import stopwords
from string import punctuation

# Download stopwords and punkt tokenizer
nltk.download('stopwords')
nltk.download('punkt')

# Load stop words and punctuations
stop_words = set(stopwords.words('english'))
punctuations = set(punctuation)

def preprocess_text(text):
    # Lowercase conversion
    text = text.lower()
    # Tokenization
    tokens = nltk.word_tokenize(text)
    # Remove stopwords and punctuations
    tokens = [word for word in tokens if word not in stop_words and word not in punctuations]
    # Join tokens to form text string
    text = preprocessed_text(' '.join(tokens))
    return preprocessed_text

labels =['positive', 'negative', 'positive', 'positive', 'negative', 'positive', 'negative', 'negative', 'positive', 'positive']

df = pd.DataFrame({'review':text, 'sentiment': labels})

X_train, X_test, y_train, y_test = train_test_split(df['review'], df['sentiment'], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

"""naive bayes"""

nb = MultinomialNB()
nb.fit(X_train_vec, y_train)

y_pred = nb.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer

pipeline = Pipeline([
    ('vectorizer', CountVectorizer(lowercase=True, stop_words='english', strip_accents='unicode')),
    ('classifier', MultinomialNB())
])

scores = cross_val_score(pipeline, df['review'], df['sentiment'], cv=3)

print(scores)

"""knn

"""

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

X_train, X_test, y_train, y_test = train_test_split(df['review'], df['sentiment'], test_size=0.2, random_state=42)

knn.fit(X_train_vec, y_train)

# Predict the sentiment of the test data
y_pred = knn.predict(X_test_vec)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

"""deployment"""

import pickle
pickle.dump(new_df,open('df.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))

new_df['title'].values

new_df.to_dict()

pickle.dump(new_df.to_dict(), open('df_dict.pkl','wb'))

!pip install streamlit

!pip install -q streamlit

!./ngrok authtokens your_token

!pip install pyngrok

from pyngrok import ngrok 
public_url = ngrok.connect(port='8501')
public_url

# Commented out IPython magic to ensure Python compatibility.
# %%writefile streamlit_app.py 
# import streamlit as st 
# st.markdown("" This is a Streamlit App """)

!streamlit run /content/streamlit_app.py & npx localtunnel — port 8501

import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
  movie_index = tags[tags['title']== movie].index[0]
  recom = similarity[movie.index]
  movie_list = sorted(list(enumerate(recom)),reverse = True, key = lambda x:x[1])[1:11]

  recommended_movies = []

  for i in movie_list:
    recommended_movies.append(tags.iloc[i[0]].title)
  return recommended_movies

df_dict = pickle.load(open('df_dict.pkl','rb'))
tags = pd.DataFrame(df_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation system')

option= st.selectbox('select your movie:', tags['title'].values)

if st.button('Recommend'):
  recommendations = recommend(option)
  for i in recommendations:
    st.write(i)

!npm install localtunnel

!streamlit run app.py &>/content/logs.txt &

!npm install -g localtunnel

!lt --port 8000

!npx localtunnel --port 8501