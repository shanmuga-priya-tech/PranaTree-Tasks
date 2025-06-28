import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tabulate import tabulate

# Download VADER lexicon (it contains list of predefined words with score)
#we download it only once to avoid repeated download for every run
try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')


# Initialize VADER sentiment analyzer.create an obj from sentimentIntenistyAnalyser class
analyzer = SentimentIntensityAnalyzer()

# sample sentence
reviews = [
    "I love this product!",
    "This is the worst movie I've ever seen.",
    "The food was okay, not great.",
    "Absolutely fantastic experience.",
    "I am very disappointed.",
    "It's just average.",
    "This made me so happy!",
    "Not what I expected.",
    "Great value for the price.",
    "Would not recommend.",
    "Totally worth it!",
    "I feel bad about this.",
    "It's fine, I guess.",
    "Best day ever!",
    "I'm not sure how I feel about it."
]

# Analyze each review and collect data

#maintain a list to store review,compound score and final result
table_data = []

#loop through the sample list
for review in reviews:
    score = analyzer.polarity_scores(review)# find the  polaity score( it returns dic)
    compound = score['compound'] #extract only compound score as its the overall score
    
    # Determine final sentiment
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    # make new entry to the list
    table_data.append([review, compound, sentiment])

# Print table
headers = ["Review", "Compound Score", "Final Sentiment"]
#using tabulate to form table
print(tabulate(table_data, headers=headers, tablefmt="grid"))

''' for larger data set we should use something like pandas as it is easy for 
performing operations like aggregation,sorting,filtering and so on
tabulate is used just for display purporse
'''

