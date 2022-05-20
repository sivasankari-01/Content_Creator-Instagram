# Load Streamlit library
import streamlit as st
from PIL import Image
import pandas as pd
import csv
import instaloader
img = Image.open("logo.png")
st.image(img, width=300)
img = Image.open("instalogo.png")
image=st.image(img, width=50)
st.title('Instagram Content Creator\n',image)

st.write("\nExplore the data of Content Creator!")
# function for getting more than 5K+ followers

dataFrame_creator= pd.read_csv('final Scrap.csv')
co = dataFrame_creator['followersCount']
dataFrame_creator['followersCount'] = dataFrame_creator['followersCount'].fillna(0)
result=dataFrame_creator[dataFrame_creator['followersCount'] >= 5000]['followersCount'].count()
p=dataFrame_creator[dataFrame_creator['followersCount']>5000]
p.to_csv('Creator_morethan5K.csv')

status = st.radio("Select Option: ", ('Check the Number of followers more than 5K followers',
                                      'Check the Specific Creator from database',
                                      'Check the Creator outer from the database and check business category'))
if (status == 'Check the Number of followers more than 5K followers'):
    st.success(result)
    st.write(p)
    st.success('The creators saved in a csv file name of -Creator_morethan5K.csv')
elif (status == 'Check the Specific Creator from database'):
   btn=st.button('Enter to retrieve the whole data')
   if btn:
       global df, df1, df2
       #url1 = input("Enter the Username1:\n")
       #url2 = input("Enter the Username1:\n")
       #fit_with_ishmeet
       url1 = 'fit_with_ishmeet'
       url2 = 'mamissfitness'
       csv_reading = csv.reader(
           open('C:/Users/sivasankari/Downloads/Snipfeed/read/data/final scrap.csv', 'r', encoding="cp437"))
       data = pd.read_csv("final scrap.csv")  # path folder of the data file
       st.write(data)
       for row in csv_reading:
           if url1 == row[3]:
               a = row;
               index = ['profileUrl', 'mailFound', 'contactPhoneNumber', 'profileName', 'fullName', 'bio',
                        'followersCount', 'followingCount', 'instagramID', 'isBusinessAccount',
                        'isVerified', 'businessCategory', 'postsCount']
               ind = pd.Series(index)
               fd = ind.to_frame()
               a1 = pd.Series(row)
               df1 = a1.to_frame()
           if url2 == row[3]:
               b = row;
               b1 = pd.Series(row)
               df2 = b1.to_frame()

       # concatenate dataframes
       frames = [fd, df1, df2]
       d = pd.concat(frames, axis=1)
       print(d)
       d.to_csv('Given_User.csv', index=['Index', 'User1', 'User2'], header=False)

       if 'FALSE' in df1.values or 'FALSE' in df2.values:
           st.error('Not Having similarity - Either one or both are not an Business Account\n')
           data = pd.read_csv("Given_User.csv")  # path folder of the data file
           st.write('Both users data to compare',data)
       else:
           st.success('Having similarity between users - Both are business account\n ')
           data = pd.read_csv("Given_User.csv")  # path folder of the data file
           st.write('Both users data to compare',data)
elif(status == 'Check the Creator outer from the database and check business category'):
    bot = instaloader.Instaloader()
    #Username = input('Enter the Account Username: \n')
    Username = st.text_input('Enter the Account Username: \n')
    btn = st.button('Enter')
    if btn:

        similar = 0
        business = 0
        a = []
        b = []
        profile = instaloader.Profile.from_username(bot.context, Username)
        print("Username: ", profile.username)
        print("User ID: ", profile.userid)
        print("Number of Posts: ", profile.mediacount)
        print("Followers: ", profile.followers)
        print("Followees: ", profile.followees)
        print("Bio: ", profile.biography)
        print("Url", profile.external_url)
        print('Business Account:', profile.is_business_account)
        print('Catagory of business:', profile.business_category_name)
        data = [profile.username, profile.userid, profile.mediacount, profile.followers, profile.followees,
            profile.biography, profile.external_url, profile.is_business_account, profile.business_category_name]
        fd1 = pd.DataFrame(data, index=['Username', 'User ID', 'Number of Posts', 'Followers', 'Followees', 'Bio', 'Url',
                                   'Business Account', 'Catagory of business'])
        fd1.to_csv('newuser.csv')
        similarity1 = profile.followers
        similarity2 = profile.is_business_account
        similarity3 = profile.business_category_name
        csv_reading = csv.reader(
            open('C:/Users/sivasankari/Downloads/Snipfeed/read/data/final scrap.csv', 'r', encoding="cp437"))
        for row in csv_reading:
            if similarity2 == False:
                continue
            elif similarity3 in row[10]:
                similar += 1
                a.append(row)

            elif similarity2:
                business += 1
                b.append(row)
        data = pd.read_csv("newuser.csv")  # path folder of the data file
        st.write(data)
        st.write('Number of accounts in similar with DB accounts', similar)
        st.write('Number of Business in similar with DB accounts', business)
        data_Similar = pd.DataFrame(a)
        data_Similar.to_csv('Similar_Account.csv', index=None)
        data = pd.read_csv("Similar_Account.csv")  # path folder of the data file
        st.write(data)
        data_Business = pd.DataFrame(b)
        data_Business.to_csv('Similar_Business.csv', index=None)
        data = pd.read_csv("Similar_Business.csv")  # path folder of the data file
        st.write(data)
