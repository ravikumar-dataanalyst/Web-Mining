#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Session 7 Assignment Task 2

pip install vaderSentiment


# In[6]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Read content from the text file
file_path = "web_content.txt"
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Perform sentiment analysis
analyzer = SentimentIntensityAnalyzer()
sentiment_scores = analyzer.polarity_scores(content)

# Print sentiment scores
print("Sentiment Scores:")
print(f"Positive: {sentiment_scores['pos']}")
print(f"Neutral: {sentiment_scores['neu']}")
print(f"Negative: {sentiment_scores['neg']}")
print(f"Compound: {sentiment_scores['compound']}")

# Categorize sentiment based on the compound score
if sentiment_scores['compound'] >= 0.05:
    sentiment = "Positive"
elif sentiment_scores['compound'] <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Overall Sentiment: {sentiment}")


# # Summary : The Above code reads the text from the file web_content.txt and performs sentiment analysis. We get Overall Positive Sentimental Analysis score followed by 0.114 -Positive and Just 0.025 Negative Scores.
