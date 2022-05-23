# Content_Creator-Instagram
# Install Libraries
```
pandas==1.2.4
numpy==1.20.1
beautifulsoup4==4.11.1
GitPython==3.1.27
instaloader==4.9
jupyter==1.0.0
matplotlib-inline==0.1.3
requests==2.27.1
SQLAlchemy==1.4.36
streamlit==1.9.0
```
# Frontend Libraries
<h3>Streamlit</h3>
Please read the following guidelines for the <b>Streamlit</b> Setup:<br>
https://docs.streamlit.io/library/get-started/installation<br><br>

```angular2html
pip install streamlit
```
# RUN THIS APP LOCALLY
To run this app locally, clone the code from the <b>local branch</b> (very important). Then, set up the virtual environment in your system and run the following command:<br>
```angular2html
pip install -r requirements.txt
```
After that, run the following below servers:

# RUN STREAMLIT SERVER
```angular2html
streamlit run web_app/Streamlit.py
```
Now your app should be running on your localhost with the port 8501 depending upon your system (please check the streamlit terminal). You can access it most probably with the following link:
http://localhost:8501/ or http://127.0.0.1:8501/
# Python file and csv Description
# Python file : 
```
Streamlit.py - Main python file- Entire project code
```
```angular2html
SQL_retrive.py - Another option to get data from DB using SQL commands
```
```angular2html
Engagement.py - To calculate the engagement score
```
# CSV file : 
```angular2html
final scrap.csv - Scraped creator data
```
```angular2html
Given_User.csv - Fetch request from API, retrieve data of 2 users from database to compare the similarity between them
```
```angular2html
newuser.csv- Fetch request from API scrape the creator data not from the database(package-Instaloader) and Saved the new creator profile to a csv file
```
```angular2html
Similar_Account.csv - Fetch similar accounts details that match with the new user from database and saved 
```
```angular2html
Similar_Business.csv- Fetch similar business details that match with the new user from database and saved 
```
 # Conclution : 
```
Scrape the content creator account from instagram and sort only 5K plus followers, then took two user from database and compare their similarity and finally get a new instagaram userName(from database/ outer frfom the database), retrieve infos of a give account and check the similar accounts match with the new account. To check similarity with number of followers, engagement score , whether its a business account or not and whether match with same business
```
