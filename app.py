import streamlit as st
from src.data_preprocessing import preprocess_text

# Title of the app
st.title('Customer Sentiment Analysis')

# Text input for user
user_input = st.text_area('Enter customer feedback:', '')

# Button to analyze sentiment
if st.button('Analyze'):
    # Preprocess the input text
    processed_text = preprocess_text(user_input)
    # Placeholder for sentiment analysis result
    # Here you would call your sentiment analysis model
    sentiment_result = 'Positive'  # Example result
    
    # Display the result
    st.write('Processed Text:', processed_text)
    st.write('Sentiment:', sentiment_result)

# Footer
st.markdown('---')
st.markdown('Developed by Your Name') 