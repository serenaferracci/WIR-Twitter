import tweepy
import json

usa_location = 23424977

#Serena's keys
consumer_key = 	"MNIY1db3L8UIWbWwcIufdbLsE"
consumer_secret = "EI9DxGIM7BoJOzNHUPjTn3kIPwK8OjNTWgLeWlb46wMg5gvFmE"

access_token = "455678422-G3uLg4O7ulLaZbyVhaSa2zPZamyHjC6eUClw0hUC"
access_token_secret = "gGTh7L7O5P7EhsKiqcESXqA9RXjiafNZOrc5MVXBEap4i"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

result = api.trends_place(usa_location)
#print(type(result[0]['trends'][0]))
#for elem in result[0]['trends']:
#	print(elem)
print(result[0]['trends'][0]['name'] + "\n\n\n\n\n\n\n\n")
for tw in  tweepy.Cursor(api.search, q = result[0]['trends'][0]['name'], lang = "en", show_user = True, tweet_mode = 'extended').items(10):
	if 'retweeted_status' in dir(tw):
		print(tw.user.id)
		print(tw.retweeted_status.full_text+"\n\n")
	else:
		print(tw.user.id)
		print(tw.full_text+"\n\n")
#tw is a list, _json is a dictionary

#print(type(tw))

#for elem in tw['_json']
#	print(elem['text'])
#print(tw)
