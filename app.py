import streamlit as st
import pickle
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

# Define the vectorize_stories function

with open('chatbot_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tokenizer.pkl', 'rb') as tk:
    tokenizer = pickle.load(tk)


def vectorize_stories(data, word_index=tokenizer.word_index, max_story_len= 154,
                      max_question_len= 6 ):

    # X = STORIES
    X = []
    # Xq = QUERY/QUESTION
    Xq = []
    # Y = CORRECT ANSWER
    Y = []

    for story, query, answer in data:
        # Grab the word index for every word in story
        x = [word_index[word.lower()] for word in story]
        # Grab the word index for every word in query
        xq = [word_index[word.lower()] for word in query]

        # Grab the Answers (either Yes/No so we don't need to use list comprehension here)
        # Index 0 is reserved so we're going to use + 1
        y = np.zeros(len(word_index) + 1)

        # Now that y is all zeros and we know its just Yes/No , we can use numpy logic to create this assignment
        #
        y[word_index[answer]] = 1

        # Append each set of story,query, and answer to their respective holding lists
        X.append(x)
        Xq.append(xq)
        Y.append(y)

    # Finally, pad the sequences based on their max length so the RNN can be trained on uniformly long sequences.

    # RETURN TUPLE FOR UNPACKING
    return (pad_sequences(X, maxlen=max_story_len), pad_sequences(Xq, maxlen=max_question_len), np.array(Y))
# Load your chatbot model


# Streamlit app
st.title("Chatbot Web App")

# User input fields
story = st.text_input("Story:", "")
question = st.text_input("Question:", "")

if st.button("Ask"):
    if story and question:
        # Vectorize user input using vectorize_stories

        mydata = [(story.split(), question.split(), 'yes')]

        my_story, my_ques, my_ans = vectorize_stories(mydata)

        pred_results = model.predict(([my_story, my_ques]))

        val_max = np.argmax(pred_results[0])

        response=''

        for key, val in tokenizer.word_index.items():
            if val == val_max:
                response = key

        st.text("Chatbot:", response)

