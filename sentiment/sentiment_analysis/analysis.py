import nltk
from nltk.tokenize import word_tokenize

# Step 2
dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
  
# Step 3
t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]
# Step 4 – the classifier is trained with sample data
classifier = nltk.NaiveBayesClassifier.train(t)
  
test_data = "test"
test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}