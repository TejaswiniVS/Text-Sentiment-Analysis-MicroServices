# Text Analysis Microservices Application

This is a microservices-based application for text analysis. It allows you to register and manage multiple text analysis services and perform various text analysis tasks. The application exposes a RESTful API for interacting with these services.
Central microservice adds ,lists the microservices and interacts with text analysis microservices

## Features

- Register and manage text analysis services.
- Perform text analysis tasks, such as sentiment analysis, word count, and entity recognition.

## Technologies Used

- Python
- Flask (for the central microservice,text analysis microservices)
- TextBlob (for the text sentiment analysis microservice)
- Requests (for making HTTP requests)
- Other libraries as needed

## Installation
There are three steps of installations:
1. Downloading the repository
2. Installing the requirements
3. Running the MicroServices

**1. Downloading the repository:**
Open Terminal
```bash
$ git clone https://github.com/TejaswiniVS/Text-Sentiment-Analysis-MicroServices.git
$ cd Text-Sentiment-Analysis-MicroServices
```
**2. Installing the requirements:**

2.1. Open your terminal and navigate to the directory where your application is located.
     Inside your project directory, run the following command to install dependencies from requirements.txt file:
```
$ pip install -r requirements.txt
```
2.2. Go to every microservice folder and install dependencies from their respective requirements.txt file :
        central-main-service directory
        word-count-service directory
        sentiment-analysis-service directory

**3. Running the MicroServices:**
We need to activate the virtual enviornment for each microservice for it to run
3.1. Open new terminal tab for each microservice
3.2. Go to the directory of the microservice

```
cd $ cd central-main-service
```
3.3. Activate the virtual enviornment
```
$ pipenv shell
```     
Your terminal prompt should change to indicate that you are now working within the virtual environment.     

3.4. With the virtual environment activated, you can now run central microservice :
```
$ python centralservice.py
```
Similarly for ***Word-Count*** Service follow ***3.1 to 3.4***
```
$ cd word-count-service
$ pipenv shell
$ python wordcount.py
```
Similarly for *****Text-Sentiment Analysis***** Service follow ***3.1 to 3.4***
```
$ cd sentiment-analysis-service
$ pipenv shell
$ python sentimentservice.py
```
Similarly for ***Entity Recognition Service*** Service follow ***3.1 to 3.4*** :
```
$ cd entity-recognition-service
$ pipenv shell
$ python recognitionservice.py
```
3.5. When you're done working on your project and want to exit the virtual environment, you can run:
```
Ctrl+C
exit
```
