# data_preprocessing.py

# This script will contain functions for cleaning and preprocessing text data.

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load('en_core_web_sm')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Download stopwords
nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    # Tokenize and lemmatize
    doc = nlp(text)
    tokens = [lemmatizer.lemmatize(token.text.lower()) for token in doc if token.text not in stopwords.words('english')]
    return ' '.join(tokens)

# Example usage
def main():
    sample_text = "This is an example sentence for preprocessing."
    print("Original:", sample_text)
    print("Processed:", preprocess_text(sample_text))

if __name__ == "__main__":
    main() 