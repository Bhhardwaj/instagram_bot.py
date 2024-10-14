
import time
from instabot import Bot  # You can use the instabot package

# Create a bot instance
bot = Bot()

# Login to Instagram
def login_instagram(username, password):
    bot.login(username=username, password=password)

# Follow users from a given profile
def follow_users_from_profile(target_profile):
    user_ids = bot.get_user_following(target_profile)
    for user_id in user_ids:
        bot.follow(user_id)

# Check for follow back and unfollow non-followers
def check_follow_back():
    followers = bot.get_user_followers(bot.user_id)
    following = bot.get_user_following(bot.user_id)

    # Unfollow users who did not follow back
    for user in following:
        if user not in followers:
            bot.unfollow(user)

# Main function to run the script
def automate_following(username, password, target_profile):
    login_instagram(username, password)
    while True:
        # Follow users
        follow_users_from_profile(target_profile)
        
        # Wait for 1 hour
        time.sleep(3600)
        
        # Check for follow back and unfollow non-followers
        check_follow_back()

# Example of using the script
if __name__ == "__main__":
    my_username = "your_instagram_username"
    my_password = "your_instagram_password"
    target_profile_username = "target_profile_username"
    
    automate_following(my_username, my_password, target_profile_username)
