# Reddit-Flair-Detector

A web application to predict flair (tag) of any post on [India Subreddit](https://www.reddit.com/r/india) using Machine Learning Algorithms.
The application can be found live at [Reddit Flair Detector](https://redditflair-detector.herokuapp.com).
   
## Execution Instructions
1. Download Git Large File Storage (LFS) from https://git-lfs.github.com/ if you don't have it already.
2. Open the Terminal.
3. Use ``` git lfs install ``` to set up Git LFS for your user account.
4. Clone the repository by typing ``` git clone https://github.com/Gunnika/Reddit-Flair-Detector.git ```.
5. Ensure that Python3 and pip are installed on the device.
6. Change to the cloned directory by entering ```cd Reddit-Flair-Detector ```.
7. Run ```pip install -r requirements.txt```.
8. Enter the python shell and ``` import nltk ```.
9. Execute ``` nltk.download('stopwords')``` and ``` nltk.download('punkt')```. Exit the shell.
10. Run ``` python app.py``` to start the application on a local host.
11. Go to http://0.0.0.0:5000/ on the web browser to use the application.

## Work Flow
0. [Data Aquisition](#data-acquisition)
0. [Exploratory Data Analysis](#exploratory-data-analysis)
0. [Data Pre-Processing](#data-pre-processing)
0. [Building a Flair Detector](#building-a-flair-detector)
0. [Building a Flask Application](#building-a-flask-application)
0. [Integrating WebApp and Trained Model](#integrating-webapp-and-trained-model)
0. [Deploying as a Web Service](#deploying-as-a-web-service)

### Data Acquisition
[PRAW: The Python Reddit API Wrapper](https://praw.readthedocs.io/en/latest/) was used for extracting data. There are a number of Reddit datasets available on Bigquery and Kaggle as well. 
For the purpose of creating my own dataset instead of the readily available alternatives, I went ahead with PRAW.

The following attributes made more sense in indicating the flair of a post
- title
- url
- text
- comments


### Exploratory Data Analysis
### Data Pre-Processing
### Building a Flair Detector
### Building a Flask Application
### Integrating WebApp and Trained Model
### Deploying as a Web Service
