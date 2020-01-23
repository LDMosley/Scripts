# This is my attemp to recreat the functionally of the twit_interest.py script,
# using tweepy instead of twython.
# twit_interest.py was created by Mark Baggett and can be found at:
# https://gist.github.com/MarkBaggett/c43cf2440ed63990f67613f2134f120b

from collections import Counter
import sys
import tweepy

consumer_key = 'Your Twitter Keys'
consumer_secret = 'Your Twitter Keys'

access_token = 'Your Twitter Keys'
access_token_secret = 'Your Twitter Keys'

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

if len(sys.argv) != 2:
    print(
        'Usage - Pass one argument.  The twitter profile name. Do not include the @.\n Example: "python interesTweet.py nytimes"')
    sys.exit(1)

user = api.get_user(sys.argv[1])

c = Counter()

ignore_words = ['AND', "WE", "THAT", "THAN", "THEM", 'OF', "GET", "SO", "SOME", 'THE', 'TO', 'FOR', 'MY', 'IN', 'IS',
                'ARE', 'I', 'AT', 'ON', 'WITH', 'BY', 'NOT', 'THAT', 'TWEETS', 'WE', 'ALL', 'FROM', 'OWN', 'ABOUT',
                'DO', 'YOU', 'OUR', 'THIS', 'THINGS', 'TEAM', 'YOUR', 'VIEWS', 'AN', 'TWITTER', 'THOUGHTS', 'MOST',
                'NOW', 'OPEN', 'NEW', 'THERE', 'AS', 'WHO', 'ONE', 'OR', 'ALWAYS', 'IF', 'ME', 'THOSE', 'BE', 'AM',
                'AROUND', 'LIKE', 'NO', 'SEE', 'GROUP', 'EXPRESSED', 'JUST', 'EVERY', 'BUT', 'MORE', "WHY", "BECAUSE",
                "SOLELY", "WITHIN", "SINCE", "ITS", "LOT", "OTHER", "BOTH", "UP", "HERE", "BETTER"]

ignore_chars = """.,'!-/:?"'#@"""

num = user.friends_count

print("Analyzing {} accounts...\n".format(num))

for count, friend in enumerate(tweepy.Cursor(api.friends_ids, id=sys.argv[1]).items()):
    if count % 10 == 0:
        print("\r|{0:-<50}| {1:3.2f}%".format("X" * (50 * count // num), 100 * count / num), end="")
    description = api.get_user(id=friend).description
    description = description.translate(str.maketrans("", "", ignore_chars))
    description = [x for x in description.upper().split() if x not in ignore_words and len(x) > 1]
    c.update(description)

print(c.most_common(1000))
