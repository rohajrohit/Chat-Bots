# Chat-Bots with RNN

## Overview
The Chatbot for Story-Based Question Answering is an intelligent conversational agent designed to answer questions based on stories or textual passages provided to it. This project leverages Natural Language Processing (NLP) techniques and a multi-layer Recurrent Neural Network (RNN) to generate context-aware responses.

## Key Features
Story Understanding: The chatbot reads and comprehends stories, allowing it to answer questions accurately.
Input Memory Representation: The stories are encoded into a meaningful representation that captures context and information.
Output Memory Representation: The chatbot generates an output memory representation that contains the answer and relevant context.
Multi-Layer RNN: The model employs a multi-layer RNN architecture to handle sequences and capture context at different levels.
Question Answering: The chatbot can answer a wide range of questions related to the provided stories.
Context Preservation: The chatbot maintains context across interactions, providing contextually relevant responses.

## Screenshot
Here I've attached a screenshot from my project.
<div align='center'>
    <img src='Screenshot (356).png'>
</div> 

## How It Works
Story Processing: The chatbot takes a story or passage as input and preprocesses it, converting it into an input memory representation.
Question Input: When a user asks a question, the chatbot processes the question and combines it with the input memory representation to create a context-aware query.
RNN-Based Computation: The multi-layer RNN processes the context-aware query to generate an output memory representation, which contains the answer and relevant context.
Response Generation: The chatbot extracts the answer from the output memory representation and formulates a contextually accurate response.
