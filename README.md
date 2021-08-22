# RNN API Endpoint
This is a simple python webapp written in FastAPI which provides a web based interface to a tensorflow based NLP engine running on the localhost. The objective here is to generate a random sentence or a paragrapgh starting with a word given by the user which makes some sense. It has no storage or DB of sentences, thus generating real time data with AI (RNN baased model), running with tensorflow. The design uses css from online CDN systems. It uses JQuery ajax for its requests. 
## Installation
Use pip to install (recommended in a venv)
``
pip install -r requirements.txt
``
## Running
Run this from a venv on the terminal

``
uvicorn main:app
``
Then go to http://127.0.0.1:8000/ and enter a word (of any length) in the form and hit enter
## Screenshots
From http://127.0.0.1:8000/
![The UI](https://github.com/Sumalyo/RNN-API-Endpoint/blob/main/RNN-API-SS.png)

