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

2.1. Open your terminal and navigate to the  directory where your application is located.
    Inside your project directory- Text-Sentiment-Analysis-MicroServices , run the following command to install dependencies from requirements.txt file:
```
$ pip install -r requirements.txt
```

**3. Running the MicroServices:**
We need to activate the virtual enviornment for each microservice for it to run
3.1. Open new terminal tab for each microservice
3.2. Go to the directory of the microservice

```
cd $ cd central-main-service
```
3.3. Activate virtual enviornment:
```
$ pipenv shell
```
3.4. Install the dependencies from requirements.txt file:
```
pip install -r requirements.txt
```
3.5. With the virtual environment activated, you can now run central microservice :
```
$ python centralservice.py
```
Similarly for ***Word-Count*** Service follow ***3.1 to 3.5***
```
$ cd word-count-service
$ pipenv shell
pip install -r requirements.txt
$ python wordcount.py
```
Similarly for *****Text-Sentiment Analysis***** Service follow ***3.1 to 3.4***
```
$ cd sentiment-analysis-service
$ pipenv shell
pip install -r requirements.txt
$ python sentimentservice.py
```
Similarly for ***Entity Recognition Service*** Service follow ***3.1 to 3.4*** :
```
$ cd entity-recognition-service
$ pipenv shell
pip install -r requirements.txt
$ python recognitionservice.py
```
3.5. When you're done working on your project and want to exit the virtual environment, you can run:
```
Ctrl+C
exit
```
## Usage

Access the application opening a POSTMAN and navigating to http://localhost:8000/services.
All services will be listed.

Based on the service name("name") we will perform the respective text analysis . 

Perform text analysis tasks by sending POST requests to '/analyze' API with payload -service and text to analyze. See the API documentation below for details.
## API Documentation:

## Central MicroService
**List Registered Services**
Endpoint: /services
Method: GET
Response: JSON array containing the list of registered services

**Analyze Text Services**

Endpoint: /analyze
Method: POST
Request Body: JSON object with service name and text to analyze (service, text)
Response: JSON response with analysis result 

**Register a Service**
Endpoint: /services
Method: POST
Request Body: JSON object with service details (name, port, url)
Response: JSON response with registration status

## Word-Count MicroService
**WordCount**
Endpoint: /count
Method: POST
Request Body: JSON object with text to analyze (text)
Response: JSON response ,count of words present in text

## Sentiment-Analysis MicroService
**SentimentAnalysis**
Endpoint: /sentiment
Method: POST
Request Body: JSON object with text to analyze (text)
Response: JSON response ,analysis if the text sentiment is positive,negative,neutral

## Entity Recognition MicroService
**Recognition**
Endpoint: /entity
Method: POST
Request Body: JSON object with text to analyze (text)
Response: JSON response ,analysis if the text with classification and identification of entities
