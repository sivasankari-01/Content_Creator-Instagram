import instaloader
from instaloader import Profile
#Used these code to calculate the engagement score
bot = instaloader.Instaloader()
target_profile = 'sivasankari287' #here you can use SNIPFEED insta account
profile = Profile.from_username(bot.context, target_profile)
num_followers = profile.followers
total_num_likes = 0
total_num_comments = 0
total_num_posts = 0

for post in profile.get_posts():
    total_num_likes += post.likes
    total_num_comments += post.comments
    total_num_posts += 1

print(total_num_likes,total_num_posts,total_num_comments,num_followers)
engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
print(engagement * 100)
