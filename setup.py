from setuptools import setup, find_packages

setup(
    name='customer_sentiment_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk',
        'spacy',
        'tensorflow',
        'flask',
        'jupyter'
    ],
    description='A project for customer sentiment analysis using NLP',
    author='Your Name',
    author_email='your.email@example.com'
) 