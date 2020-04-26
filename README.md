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
0. [Deploying as a Web Service](#deploying-as-a-web-service)

The whole process is nicely explained with code in this [Jupyter Notebook](https://github.com/Gunnika/Reddit-Flair-Detector/blob/master/Jupyter%20Notebooks/Reddit%20Flair%20Detector.ipynb).

### Data Acquisition
[PRAW: The Python Reddit API Wrapper](https://praw.readthedocs.io/en/latest/) was used for extracting data. There are a number of Reddit datasets available on Bigquery and Kaggle as well. 
For the purpose of creating my own dataset instead of the readily available alternatives, I went ahead with PRAW.

The following attributes made more sense in indicating the flair of a post
- title
- url
- text
- comments


### Exploratory Data Analysis
Initial investigations of data included analysing the data distribution amongst classes wherein an imbalanced distribution was observed. The [R]eddiquette class had low data as compared to the other classes which can result in the minority class being treated as outlier and ignored.

![Imbalanced Classes](https://github.com/Gunnika/Reddit-Flair-Detector/blob/master/Images/imbalanced.png)

The reason for this imbalance was found to be discontinuation of the [R]eddiquette flair 7 months ago.
The class was then dropped from the dataset


### Data Pre-Processing
The Data pre-processing step involved cleaning the data for better representation and usability. In this:
- The stop words were removed
- words tokenized 
- words converted into lowercase
- Useful words concatenated to a sentence

### Building a Flair Detector
Different models analysed:
- Logistic Regression
- Linear Support Vector Machine
- Naive Bayes Classifier
- Decision Trees
- Random forest

![Models Trail Summary](https://github.com/Gunnika/Reddit-Flair-Detector/blob/master/Images/train.png)


The best results were obtained using Random Forest.

### Building a Flask Application
A flask application was developed in which the trained model was integrated. An automated_testing endpoint was generated for automatic retrieval of predictions by providing a text file of urls.

### Deploying as a Web Service
The application was then deployed to Heroku. 
![Web App](https://github.com/Gunnika/Reddit-Flair-Detector/blob/master/Images/webapp.png)
