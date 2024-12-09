# Aspect based sentiment analysis
pip install textblob

import nltk
nltk.download('punkt')

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob
import matplotlib.pyplot as plt
from collections import Counter
import re

# Load the dataset
file_path = "C://Users//meghn//Downloads//Cleaned_Dolche_Vita_Reviews.csv"  
reviews = pd.read_csv(file_path)

# Ensure consistent column naming
reviews.columns = reviews.columns.str.strip()

# Focus on reviews with ratings <= 2
low_rating_reviews = reviews[reviews['Rating'] <= 2]

# Combine all reviews into a single text for keyword analysis
low_rating_text = " ".join(low_rating_reviews['Review'].astype(str))

# Tokenize and clean the text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    return text

cleaned_text = clean_text(low_rating_text)





# Define aspect keywords
aspects = {
    'food': ['food', 'dish', 'meal', 'menu', 'taste', 'cuisine'],
    'service': ['service', 'staff', 'waiter', 'manager', 'server'],
    'ambiance': ['ambiance', 'atmosphere', 'decor', 'music', 'environment'],
    'value': ['value', 'price', 'cost', 'expensive', 'cheap']
}

# Count occurrences of each aspect keyword in reviews
aspect_counts = {aspect: 0 for aspect in aspects}
for aspect, keywords in aspects.items():
    for keyword in keywords:
        aspect_counts[aspect] += cleaned_text.count(keyword)

print("Aspect Counts:", aspect_counts)





# Sentiment analysis for each aspect
def analyze_aspect_sentiment(reviews, aspect_keywords):
    sentiments = []
    for review in reviews:
        if any(keyword in review for keyword in aspect_keywords):
            sentiment = TextBlob(review).sentiment.polarity
            sentiments.append(sentiment)
    return sentiments

aspect_sentiments = {aspect: analyze_aspect_sentiment(low_rating_reviews['Review'], keywords)
                     for aspect, keywords in aspects.items()}

# Calculate average sentiment for each aspect
average_sentiments = {aspect: sum(scores) / len(scores) if scores else 0
                      for aspect, scores in aspect_sentiments.items()}

print("Average Aspect Sentiments:", average_sentiments)




# Bar chart for aspect counts
plt.figure(figsize=(10, 5))
plt.bar(aspect_counts.keys(), aspect_counts.values(), alpha=0.7)
plt.title('Frequency of Aspects in Low-Rated Reviews')
plt.xlabel('Aspect')
plt.ylabel('Count')
plt.show()

# Bar chart for average sentiment scores
plt.figure(figsize=(10, 5))
plt.bar(average_sentiments.keys(), average_sentiments.values(), color='orange', alpha=0.7)
plt.title('Average Sentiment for Aspects')
plt.xlabel('Aspect')
plt.ylabel('Sentiment Score')
plt.show()







