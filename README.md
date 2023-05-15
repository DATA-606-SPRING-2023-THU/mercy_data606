# Data Science Capstone project

**Author:** Mercy Subramani

**Semester:** Spring 2023
  
# Netflix Recommendation System

**Abstract**

In this present era, the amount of streaming videos in OTT platforms are drastically increasing. Hence it should not be a struggle for the users to search an interesting movie or tv show. This problem can be solved only by making strong recommendation system. Therefore, this project is an attempt to build a robust recommendation system using cosine similary, collaborative filtering techniques and someother Machine learning algorithms by Preprocessing data with Stemming, Vectorization and Tokenization techniques. In addition to that, Sentiment Analysis on reviews had been done to analyze users sentiments to the movies. And sucessfuly built recommendation system which recommends the very close similar movies to the users. The important variables used from the dataset to recommend movies are, Description, Genres, Ratings, Director and cast.


**Introduction**

Netflix was found in 1998 and still maintains first place in the OTT market. In the past days, people used DVD to watch movies, now we watch through
online streaming. Growth of Technologies and innovations in every field help people in various ways. Hence decided to analyze netflix recommendation engine because 
of its unique algorithm. It is the key player of the success of netflix which keeps them going.

There are so many entertaining websites in this world. For example, Amazon is a platform for different fields like AWS, prime video, Amazon music, shopping etc.
But Netflix streams only movies and tv shows with full customer satifaction and this got my attention. Because they carefully analyze reviews and ratings from the users.  


**Data source**

•	My dataset was taken from DataWorld

• link - https://data.world/bshen10921/netflix
 
• There are 12 columns and 7789 rows inthe dataset.

• Data size is 2.76 mb

• There movies and tv shows from 1947 to 2021.


**Data Description**

•	Show_id - Unique Id for movies

•	Type - shows whether movie or TV show

•	Title - title of the movie

• Director - name of the Director

•	Cast - Actor and Actress name

•	Country - country where the movie was shot

•	Date_added - when movie was added in netflix

•	Release_year - when movie was released

•	Rating - rating for the movie

•	Duration - hours of the movie

• Genres - shows the kind of movie

•	Description - Explains shortly about the movie


**Methodology**

1) Cleaned data and Performed EDA to analyze the dataset

2) Preprocessed data using Stemming, Vectorization and Tokenization techniques

3) Performed Cosine similarity technique to find similarities between movies 

4) Done Sentiment Analysis on reviews by scraping google to analyze the sentiment of user to movies

5) Performed some Machine learning algorithm using sentiment analysis to find the accuracy

6) Deployed the models using Streamlit


**Analyzed Unit**

•	Description

• Ratings

•	Genres

•	Directors

•	cast 


**Techniques/models**

•	KNN clustering

•	Naive Bayes

•	Cosine similarity


**Deployment**

Deployed the models using Streamlit



**Reference**

i) https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7975207

ii) https://link.springer.com/chapter/10.1007/978-1-4899-7637-6_11

iii) http://www.few.vu.nl/~sbhulai/papers/paper-fernandez.pdf

iv) https://www-cs.stanford.edu/people/nipunb/CS345a.pdf
