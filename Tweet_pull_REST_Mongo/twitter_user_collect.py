import pymongo
from pymongo import MongoClient
import json
import twitter
from pprint import pprint
import pandas as pd

CONSUMER_KEY = "Input the consumer key"
CONSUMER_SECRET = "Input the consumer secret key"
OAUTH_TOKEN = "Input the access token"
OAUTH_TOKEN_SECRET = "Input the secret access token"

###authorisation

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)


###setting up the mongo client to create and access the db
client = MongoClient()

### to initialise the db
db = client.user_collect

### to initialise the collection, new collection can be created by changing the collection name
sunpharma_collection = db.sunpharma_collection
sunpharma_collection.create_index([("id", pymongo.ASCENDING)], unique=True)

### count: is the number of tweets that need to be pulled
### q: the keyword on which the tweets are obtained
count = 150
q = "sunpharma"
search_results = twitter_api.search.tweets(count=count, q=q)
# pprint(search_results['search_metadata'])


statuses = search_results["statuses"]
print(statuses)
since_id_new = statuses[-1]['id']

final = []
for statues in statuses:
    try:
        ID = statues['id']
        date = statues['created_at']
        text = statues['text']
        retweet = statues['retweet_count']
        temp = {'id': ID,
                'Date': date,
                'TEXT': text,
                'Retweet_count': retweet}
        final.append(temp)
        # HDFC_collection.insert_one(statues)
        # tweet_collection.insert(statues)

    except:
        pass


df = pd.DataFrame(final)
print(df)
df.to_csv(r'C:\Users\nithi\PycharmProjects\NEW_latest\Aarna_Python_Basics\tweet_table.csv')

df_dict = df.to_dict('records')
print(df_dict)

### data that is pulled is converted to a proper format and then pushed to its respective collection in the database
sunpharma_collection.insert_many(df_dict)



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