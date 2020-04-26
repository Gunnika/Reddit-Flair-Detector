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
