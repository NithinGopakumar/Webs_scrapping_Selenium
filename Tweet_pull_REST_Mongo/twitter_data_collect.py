import json
import oauth2 as oauth
import key_token
import pandas as pd
import psycopg2
import pymongo
from pymongo import MongoClient

###authorisation
consumer = oauth.Consumer(key=key_token.consumer_key , secret=key_token.consumer_secret)
access_token = oauth.Token(key=key_token.access_token , secret=key_token.access_token_secret)
twitter_api = oauth.Client(consumer, access_token)

###setting up the mongo client to create and access the db
client = MongoClient()

### database creation
db = client.data_collect

### creating the collection
ITC_collection = db.ITC_collection
ITC_collection.create_index([("id", pymongo.ASCENDING)], unique=True)

### endpoint api for pulling the tweets of a particular user. 
### screen_name : name of the page or user whose data we have to pull
### count = the number of tweets to be pulled
endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=ITCCorpCom&count=200"

response , data = twitter_api.request(endpoint)

tweets = json.loads(data)
print(tweets)


final = []
for tweet in tweets:
    try:
        ID = tweet['id']
        date = tweet['created_at']
        text = tweet['text']
        retweet = tweet['retweet_count']
        temp = {'id': ID,
                'Date': date,
                'TEXT': text,
                'Retweet_count': retweet}
        final.append(temp)
        # tweet_collection.insert_one(tweet)
        # tweet_collection.insert(statues)

    except:
        pass

df = pd.DataFrame(final)
print(df)
df.to_csv(r'C:\Users\nithi\PycharmProjects\NEW_latest\Aarna_Python_Basics\tweet_table.csv')

df_dict = df.to_dict('records')
print(df_dict)

### data that is pulled is converted to a proper format and then pushed to its respective collection in the database
ITC_collection.insert_many(df_dict)




### to view the data that has been pushed to the db.
tweet_cursor = tweet_collection.find()
 # print(tweet_collection.count_documents())
user_cursor = tweet_collection.distinct("user.id")
print(len(user_cursor))

for document in tweet_cursor:
    try:
        print('-----')
        print('NAME :', document["user"]["name"])
        print('TEXT :', document["text"])
        print('Created Date :', document["created_at"])
    except:
        print("Error in Encoding")
        pass